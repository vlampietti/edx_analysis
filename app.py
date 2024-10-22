import dash
from dash.dependencies import Input, Output
import dash_html_components as dhc
import dash_core_components as dcc
import plotly.offline as py
import pandas as pd
import numpy as np
from plotly.widgets import GraphWidget
from datetime import datetime, timedelta
from pandas.api.types import is_string_dtype
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from plotly import tools
from pandas.io import gbq

import plotly
#plotly.offline.init_notebook_mode()

#from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

app = dash.Dash('Dash for EdX Analysis')

#df = pd.read_csv('sample_data/data_person_course.csv')
#pcd = pd.read_csv('sample_data/data_person_course_day.csv')
#sasby = pd.read_csv('sample_data/data_show_ans_stat_by_user.csv')

bgq_key = pd.read_csv('bgq_key.csv')
bgq_key = str(bgq_key.bgq_key)
bgq_key = str(bgq_key[5:24])

project_id=bgq_key

quantiles = """SELECT *
FROM `deidentified_data.person_course`"""
df = gbq.read_gbq(query=quantiles, dialect ='standard', project_id=project_id)

quantiles = """SELECT *
FROM `deidentified_data.person_course_day`"""
pcd = gbq.read_gbq(query=quantiles, dialect ='standard', project_id=project_id)

quantiles = """SELECT *
FROM `deidentified_data.show_ans_stat_by_user`"""
sasby = gbq.read_gbq(query=quantiles, dialect ='standard', project_id=project_id)


BACKGROUND = 'rgb(230, 230, 230)'

COLORSCALE = [ [0, "rgb(244,236,21)"], [0.3, "rgb(249,210,41)"], [0.4, "rgb(134,191,118)"], 
                [0.5, "rgb(37,180,167)"], [0.65, "rgb(17,123,215)"], [1, "rgb(157, 48, 165)"] ]


def scatter_plot_2d(
        x = df['nshow_answer'],
        y = df['nvideo'],
        color = df['ndays_act'],    
        xlabel = 'nshow_answer',
        ylabel = 'nvideo',
        title='All Users',
        plot_type = 'scatter',
        marker = '' ):

    data = [ dict(
        x = x,
        y = y,
        mode = 'markers',
        marker = dict( 
                colorscale = COLORSCALE,
                colorbar = dict( title = "ndays_act"),
                line = dict( color = '#444' ),
                reversescale = False,   
                sizemode = 'diameter',
                opacity = 0.7,                
                size = 12,    
                color = color
            ),
        text = df['user_id'],
        type = plot_type,      
    ) ]

  
    layout = go.Layout(title = 'All Users',
                      xaxis=dict(
                           title='nshow_answer',
                           type = 'log'),
                       yaxis=dict(
                           title='nvideo',
                           type = 'log'),
                      hovermode = 'closest',
                      margin = dict( r=0, t=0, l=0, b=0 ),
                      showlegend = False
                      )
    
    return dict( data=data, layout=layout )

def simple_donut(uid):
    user = sasby[sasby.user_id==int(uid)]
    current_user = user.groupby('user_id').sum().reset_index()

    attempted = int(current_user.n_attempted[0])
    
    hoverinfo = 'label+percent+name'
    hole = 0.4
        
    incorrect = int(current_user.n_attempted[0]) - int(current_user.n_partial[0])
    partially_correct = int(current_user.n_partial) - int(current_user.n_perfect)
    correct = int(current_user.n_perfect)
    
    labels1 = ['Incorrect','Partially Correct','Correct']
    values1 = [incorrect, partially_correct, correct]

    marker1 = dict(colors=['rgba(163, 203, 56, 1)','rgba(18, 137, 167, 1)','rgba(87, 88, 187, 1)'])
    
    name1 = 'User {}'.format(uid)
    
    domain1 = dict(x=[0,0.45],
                   y=[0,1])
    
    trace1 = go.Pie(labels=labels1,
                    values=values1,
                    hoverinfo=hoverinfo,
                    hole=hole,
                    domain=domain1,
                    marker=marker1,

                    name=name1)
    
    avg_user = sasby.mean()
    
    avg_attempted = int(avg_user.n_attempted)
        
    avg_incorrect = int(avg_user.n_attempted) - int(avg_user.n_partial)
    avg_partially_correct = int(avg_user.n_partial) - int(avg_user.n_perfect)
    avg_correct = int(avg_user.n_perfect)
    
    labels2 = ['Incorrect','Partially Correct','Correct']
    values2 = [avg_incorrect, avg_partially_correct, avg_correct]
    
    marker2 = dict(colors=['rgba(163, 203, 56, 0.7)','rgba(18, 137, 167, 0.7)','rgba(87, 88, 187, 0.7)'])
    
    name2 = 'Average Student'
    
    domain2 = dict(x=[0.55,1],
                   y=[0,1])
    
    trace2 = go.Pie(labels=labels2,
                    values=values2,
                    hoverinfo=hoverinfo,
                    hole=hole,
                    marker=marker2,
                    domain=domain2,
                    name=name2)
    
    layout = go.Layout(title="Problem Distribution",
                       showlegend=False,
                       hovermode = 'closest',
                       )
    
    data = [trace1,trace2]
    
    return dict(data = data, layout = layout)


def barchart(uid):
    
    user = sasby[sasby.user_id==int(uid)]
    current_user = user.groupby('user_id').sum().reset_index()
    
    attempted = float(current_user.n_attempted)

    incorrect = float(current_user.n_attempted) - float(current_user.n_partial)
    partially_correct = float(current_user.n_partial) - float(current_user.n_perfect)
    correct = float(current_user.n_perfect)
    
    sa_incorrect = float(current_user.n_show_answer_attempted) - float(current_user.n_show_answer_partial)
    sa_partially_correct = float(current_user.n_show_answer_partial) - float(current_user.n_show_answer_perfect)
    sa_correct = float(current_user.n_show_answer_perfect)
    
    if partially_correct > 0:
        pct_sa_partially_correct = int((sa_partially_correct / partially_correct) * 100)
    else:
        pct_sa_partially_correct = 0
    if correct > 0:
        pct_sa_correct = int((sa_correct / correct) * 100)
    else:
        pct_sa_correct = 0
    if incorrect > 0:
        pct_sa_incorrect = int((sa_incorrect / incorrect) * 100)
    else:
        pct_sa_incorrect = 0
    
    avg_user = sasby.mean()
    
    avg_attempted = float(avg_user.n_attempted)
        
    avg_incorrect = float(avg_user.n_attempted) - float(avg_user.n_partial)
    avg_partially_correct = float(avg_user.n_partial) - float(avg_user.n_perfect)
    avg_correct = float(avg_user.n_perfect)
    
    avg_sa_incorrect = float(avg_user.n_show_answer_attempted) - float(avg_user.n_show_answer_partial)
    avg_sa_partially_correct = float(avg_user.n_show_answer_partial) - float(avg_user.n_show_answer_perfect)
    avg_sa_correct = float(avg_user.n_show_answer_perfect)
    
    avg_pct_sa_partially_correct = int((avg_sa_partially_correct / avg_partially_correct) * 100)
    avg_pct_sa_correct = int((avg_sa_correct / avg_correct) * 100)
    avg_pct_sa_incorrect = int((avg_sa_incorrect / avg_incorrect) * 100)

    
 
    xlabels = ['Correct Problems', 'Partially Correct Problems', 'Incorrect Problems']
    trace1 = go.Bar(
    x=xlabels,
    y=[pct_sa_correct, pct_sa_partially_correct, pct_sa_incorrect],
    marker=dict(
        color=['rgba(87, 88, 187, 1)','rgba(18, 137, 167, 1)','rgba(163, 203, 56, 1)']),
    name='User {}'.format(uid))
    
    trace2 = go.Bar(
    x=xlabels,
    y=[avg_pct_sa_correct, avg_pct_sa_partially_correct, avg_pct_sa_incorrect],
        marker=dict(
        color=['rgba(87, 88, 187, 0.5)','rgba(18, 137, 167, 0.5)','rgba(163, 203, 56, 0.5)']),
    name='Average Student')
    
    data = [trace1, trace2]
    layout = go.Layout(
    yaxis=dict(
        range=[0,100]),
    xaxis=dict(
        tickfont=dict(
            size=10)),
    barmode='group',
    title='Percentage of Show Answer',
    showlegend=False)
       
    return dict(data = data, layout = layout)

np_username = np.array(df['username'])
np_user_id = np.array(df['user_id'])

user_array = []
count=0

while count < 745:
    user_array+=[[np_username[count],np_user_id[count]]]
    count+=1

total = pcd.groupby('date').mean()


def update(uid):
    
    for x in user_array:
        if x[1] == int(uid):
            uname = (x[0])
    #return uname
    
    uname = uname[1:]
    
    user = pcd[pcd.username==uname]
    user_total = user.groupby('date').sum().reset_index()
    user_total.loc[:,('date')] = pd.to_datetime(user_total['date'])

    date_init = datetime(2016,9,1)
    date_last =  datetime(2016,12,29)

    user_days = user_total[(user_total.date >= date_init) & (user_total.date < date_last)]
    
    all_users = total.groupby('date').sum().reset_index()
    all_users.loc[:,('date')] = pd.to_datetime(all_users['date'])
    
    total_days = all_users[(all_users.date >= date_init) & (all_users.date < date_last)]
    
    trace0 = go.Scatter(x=user_days.date,
                    y=user_days.nvideo,
                    text=user_days.date,
                    marker=dict(
                        color='rgb(249,210,41)'),
                    name='videos')
    trace1 = go.Scatter(x=total_days.date,
                    y=total_days.nvideo,
                    text=total_days.date,
                    marker=dict(
                        color='rgba(249,210,41, 0.5)'),
                    line = dict(
                        width = 2,
                        dash = 'dot'),
                    name='videos average')
    trace2 = go.Scatter(x=user_days.date,
                    y=user_days.nproblems_answered,
                    text=user_days.date,
                    marker=dict(
                        color='rgb(37,180,167, 14)'),
                    name='problems')
    
    trace3 = go.Scatter(x=total_days.date,
                    y=total_days.nproblems_answered,
                    text=total_days.date,
                    marker=dict(
                        color='rgba(37,180,167, 0.5)'),
                    line = dict(
                        width = 2,
                        dash = 'dot'),
                    name='problems average')
    trace4 = go.Scatter(x=user_days.date,
                    y=user_days.nshow_answer,
                    text=user_days.date,
                    marker=dict(
                        color='rgb(54,50,153)'),
                    name='show answer')
    trace5 = go.Scatter(x=total_days.date,
                    y=total_days.nshow_answer,
                    text=total_days.date,
                    marker=dict(
                        color='rgba(54,50,153, 0.5)'),
                    line = dict(
                        width = 2,
                        dash = 'dot'),
                    name='show answer average')

    data = [trace0,trace1,trace2,trace3,trace4,trace5]

    layout = dict(
        title='Problem Activity for User {}'.format(uid),
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                dict(count=3,
                     label='3d',
                     step='day',
                     stepmode='backward'),
                dict(count=7,
                     label='1w',
                     step='day',
                     stepmode='backward'),
                dict(count=21,
                    label='3w',
                    step='day',
                    stepmode='backward'),
                dict(count=42,
                    label='6w',
                    step='day',
                    stepmode='backward'),
                dict(step='all')
                ])
            ),
            rangeslider=dict(),
        type='date'
        )
    )
    
    return dict(data = data, layout = layout)


FIGURE = scatter_plot_2d()
STARTING_USER = 534617
SIDE_PLOT = simple_donut(STARTING_USER)
BAR_CHART = barchart(STARTING_USER)
TIMESERIES = update(STARTING_USER)
USER_DESCRIPTION = df.loc[df['user_id'] == STARTING_USER].iloc[0]

app.layout = dhc.Div([
    dhc.Link(
        rel="stylesheet",
        href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
    ),     
    dhc.Link(
        rel="stylesheet",
        href="//fonts.googleapis.com/css?family=Raleway:400,300,600"
    ),

    # Row 1: Header and Intro text
        
    dhc.Div([
                
        dhc.Div([
            dhc.H2('Dash for EdX Analysis'),
            dhc.P('SELECT a user in the dropdown menu or from the graph.'),                        
            ], className="col-md-6" ),
        
        dhc.Div([
            dhc.Br(),
            dcc.Dropdown(id='user_dropdown', 
                        multi=False,
                        value=STARTING_USER,
                        options=[{'label': i, 'value': i} for i in df['user_id'].tolist()]),
            ], className="col-md-6" )
    ], className='container' ),


    # Row 2: Hover Panel and Graph
      
    dhc.Div([
        
        dhc.Div([           
            
            
            dcc.Graph(id='clickable-graph', 
                      style=dict(height='600px'),
                      clickData=dict( points=[dict(pointNumber=0)] )),                                            
                        
        ], className='col-md-7'),
        
        dhc.Div([ 
            
            dcc.Graph(id='donut-graph', 
                      style=dict(height='300px'),
                      figure=SIDE_PLOT ),
            
            dhc.P('The darker-colored donut chart and bars represent the individual user - the lighter-colored ones represent the average.'),
            
            dcc.Graph(id='bar-chart',
                     style=dict(height='300px'),
                      figure=BAR_CHART
                     ),
        ], className="col-md-5") 
                
    ], className='container'),

    
    dhc.Div([
        dcc.Graph(id='timeseries-graph', 
                  figure=TIMESERIES )
    ])
            
], className = 'container')


@app.callback( 
    Output('user_dropdown', 'value'),
    [Input('clickable-graph', 'clickData')])
def return_user( clickData ):
    if clickData is not None:
        if 'points' in clickData:    
            firstPoint = clickData['points'][0]
            if 'pointNumber' in firstPoint:
                point_number = firstPoint['pointNumber']
                user_name = str(FIGURE['data'][0]['text'][point_number]).strip()
                print(user_name)
                return user_name


@app.callback( 
    Output('donut-graph', 'figure'),
    [Input('user_dropdown', 'value')])
def user_donuts( user_dropdown_value ):
    donut = simple_donut( user_dropdown_value )
    return donut


@app.callback( 
    Output('bar-chart', 'figure'),
    [Input('user_dropdown', 'value')])
def user_bar( user_dropdown_value ):
    bar = barchart( user_dropdown_value )
    return bar


@app.callback( 
    Output('clickable-graph', 'figure'),
    [Input('user_dropdown', 'value')])
def highlight_user( user_dropdown_value ):

    traces = [go.Scatter(
            x = df['nshow_answer'],
            y = df['nvideo'],
            text = df['user_id'], 
            name='User',
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'colorscale' : COLORSCALE,
                'reversescale' : False,
                'color': df['ndays_act'],
                'colorbar' : dict( title = "ndays_act"),
            }
        )]
    
    if user_dropdown_value is not None:
        
        print("userID: ", user_dropdown_value)

        row = df.loc[df['user_id']==int(user_dropdown_value)]

        trace_selected = go.Scatter(
            x = [row['nshow_answer'].iloc[0]],
            y = [row['nvideo'].iloc[0]],
            text=user_dropdown_value,
            showlegend=False,
            name='Selected',
            mode='markers',
            marker={
                'size': 15,
                'opacity': 1.0,
                'color' : 'black',
                'symbol' : 'x-open'
            }
        )
        traces.append(trace_selected)
    return {
        'data': traces,
        'layout': go.Layout(
            title='All Users',
            showlegend=False,
            xaxis={
                'title': 'nshow_answer',
                'type': 'log'
            },
            yaxis={
                'title': 'nvideo',
                'type': 'log'
            },
            margin={'l': 40, 'b': 40, 't': 0, 'r': 0},
            hovermode='closest'
        )
    }


@app.callback(
    Output('timeseries-graph', 'figure'),
    [Input('user_dropdown', 'value')])
def timeseries( user_dropdown_value ):
    timechart = update( user_dropdown_value )
    return timechart 


def dfRowFromClick( clickData ):
    ''' Returns row for hover point as a Pandas Series '''
    if clickData is not None:
        if 'points' in clickData:
            firstPoint = clickData['points'][0]
            if 'pointNumber' in firstPoint:
                point_number = firstPoint['pointNumber']
                user_name = str(FIGURE['data'][0]['text'][point_number]).strip()
                return df.loc[df['user_id'] == user_name]
    print(pd.Series())
    return pd.Series()


if __name__ == '__main__':
    app.server.run();
