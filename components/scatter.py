from dash import Dash,html,dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from utill import get_data

def render(app):
    df = get_data()
    fig = px.scatter(
            df, 
            x="longitude", 
            y="latitude",
            color="households"
            )
    return html.Div(dcc.Graph(figure=fig), id="scatter")

def render1(app):
    df = get_data()
    fig = px.scatter(
            df, 
            x="median_house_value", 
            y="ave_rooms",
            color="households",
            opacity=0.2
            )
    fig.update_yaxes(range=[0, 10])
    return html.Div(dcc.Graph(figure=fig), id="scatter1")