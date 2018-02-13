# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('sample_data/data_person_course.csv')

app.layout = html.Div(children=[
    html.H1(children='EdX Analysis'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(x=df.nvideos_total_watched,
                           y=df.nshow_answer,
                           text=df.username,
                           mode = 'markers')
            ],
            'layout': go.Layout(
                title='nshow_answer for nvideos_total_watched',
                xaxis={'title': 'nvideos_total_watched'},
                yaxis={'title': 'nshow_answer'},
                hovermode = 'closest'
            )

        }
    )
])



app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
