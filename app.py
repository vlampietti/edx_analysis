# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

pc = pd.read_csv('sample_data/data_person_course.csv')
pcd = pd.read_csv('sample_data/data_person_course_day.csv')

available_indicators = pcd['username'].unique()

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            figure={
                'data': [
                    go.Scatter(
                        x=pc[pc['username'] == i]['nevents'],
                        y=pc[pc['username'] == i]['nprogcheck'],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=i
                    ) for i in pc.username.unique()
                ],
                'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'nevents'},
                    yaxis={'title': 'nprogcheck'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 0},
                    hovermode='closest'
                )
        
            }
        )
    ])

])

#@app.callback(
#   dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
#    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
#    dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
#     dash.dependencies.Input('crossfilter-xaxis-type', 'value'),
#     dash.dependencies.Input('crossfilter-yaxis-type', 'value'),
#     dash.dependencies.Input('crossfilter-year--slider', 'value')])
#def update_graph(xaxis_column_name, yaxis_column_name,
#                 xaxis_type, yaxis_type,
#                 date_value):
#    pcdf = pcd[pcd['date'] == date_value]

#    return {
#        'data': [go.Scatter(
#            x=pcd[pcd['date'] == xaxis_column_name]['date'],
#            y=pcd[pcd['nevents'] == yaxis_column_name]['nevents'],
#            text=pcd[pcd['username'] == yaxis_column_name]['User Name'],
#            customdata=pcd[pcd['username'] == yaxis_column_name]['User Name'],
#            mode='markers',
#            marker={
#                'size': 15,
#                'opacity': 0.5,
#                'line': {'width': 0.5, 'color': 'white'}
#            }
#        )],
#        'layout': go.Layout(
#            xaxis={
#                'title': xaxis_column_name,
#                'type': 'linear' if xaxis_type == 'Linear' else 'log'
#            },
#           yaxis={
#                'title': yaxis_column_name,
#                'type': 'linear' if yaxis_type == 'Linear' else 'log'
#            },
#            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
#            height=450,
#            hovermode='closest'
#        )
#    }


#def create_time_series(pcdf, axis_type, title):
#    return {
#        'data': [go.Scatter(
#            x=pcd['date'],
#            y=pcd['nevents'],
#            mode='lines+markers'
#        )],
#        'layout': {
#            'height': 225,
#            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
#            'annotations': [{
#                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
#                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
#                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
#                'text': title
#            }],
#            'yaxis': {'type': 'linear' if axis_type == 'Linear' else 'log'},
#            'xaxis': {'showgrid': False}
#        }
#    }


#@app.callback(
#    dash.dependencies.Output('x-time-series', 'figure'),
#    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
#     dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
#     dash.dependencies.Input('crossfilter-xaxis-type', 'value')])
#def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
#    country_name = hoverData['points'][0]['customdata']
#    pcdf = pcd[pcd['User Name'] == username]
#    pcdf = pcdf[pcdf['User Name'] == xaxis_column_name]
#    title = '<b>{}</b><br>{}'.format(username, xaxis_column_name)
#    return create_time_series(pcdf, axis_type, title)


#@app.callback(
#    dash.dependencies.Output('y-time-series', 'figure'),
#    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
#     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
#     dash.dependencies.Input('crossfilter-yaxis-type', 'value')])
#def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
#    pcdf = pcd[pcd['User Name'] == hoverData['points'][0]['customdata']]
#    pcdf = pcdf[pcdf['User Name'] == yaxis_column_name]
#    return create_time_series(pcdf, axis_type, yaxis_column_name)



if __name__ == '__main__':
    app.run_server()