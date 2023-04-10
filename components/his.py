from dash import Dash,html,dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_data1

def render(app):
    df = get_data1()
    fig = px.histogram(df, x="median_house_value", color="ocean_proximity")
    return html.Div(dcc.Graph(figure=fig), id="his")

def render1(app):
    df = get_data1()
    fig = px.histogram(df, x="Rooms", nbins=100)
    fig.update_xaxes(range=[0, 20])
    return html.Div(dcc.Graph(figure=fig), id="his1")

