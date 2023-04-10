from dash import Dash,html,dcc
import dash_bootstrap_components as dbc
from components import scatter, his, bar

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdmPUjl9pJoF24AJOgw0nyYRjNOI6Ts9Zc4w&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrEBorWUmUeN71kKtiS7paCc5dr-z5VIKvcg&usqp=CAU"

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.H1(
                "CA House Analysis", className="header-title", style={'margin-top': '10px', 'text-align': 'center'}
              ),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'}),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"}),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'})
,       
    ],className="mt-4"),
        dbc.Row([
        html.H3("Longitude And Latitude With House Holds", className="header-title", style={'margin-top': '10px', 'text-align': 'center'}),
            dbc.Col(scatter.render(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
        html.H3('Median Price vs Average Number of Rooms', className="header-title", style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(scatter.render1(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
        html.H3("Average Distribution of Median Price", className="header-title", style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(his.render(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
        html.H3("Distribution of Average Number of Rooms", className="header-title", style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(his.render1(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
        html.H3("Ocean_proximity With Median_house_value", className="header-title", style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(bar.render(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'})
        ],className="mt-4"),
    ])