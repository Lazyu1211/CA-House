from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_ocean

def render(app):
    df = get_ocean()
    fig = px.bar(
                df,
                x="ocean_proximity",
                y="median_house_value",
                color="ocean_proximity")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume")