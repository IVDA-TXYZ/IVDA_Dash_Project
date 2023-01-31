from dash import Dash, dcc, html, Input, Output, ctx
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as ps
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import numpy as np


import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

df = pd.read_csv('Datasets/Final_Dataset.csv')

dff2 = pd.read_csv('Datasets/Final_Dataset.csv')

continues_attributes = ['duration_s', 'year',
       'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo']


y_axis_choices = ['popularity', 'danceability',  'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'tempo', 'valence']
x_axis_choices = y_axis_choices
x_axis_choices.append('year')
categorical_attributes = ['artist', 'song', 'explicit', 'genre']
advanced_chart_titles = ['Pairwise Correlation', 'Treemap', 'Total Songs by Genre', 'Popularity by Genre', 'Scatterplot Matrix', 'Feature Distribution']

import pickle
with open('Datasets/count_list.pickle', 'rb') as handle:
    genre_counts = pickle.load(handle)

app = Dash(external_stylesheets=[dbc.themes.LUX])
def drawText(text='Text', header=1, with_card=True, color='white'):
    head_map = {1: html.H1(text), 2: html.H2(text), 3: html.H3(text), 4: html.H4(text), 5: text}
    if with_card:
        return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    head_map[header],
                ], style={'textAlign': 'center'}) 
            ]), color=color, 
        ),
    ])
    else:
        return html.Div([
        # dbc.Card(
        #     dbc.CardBody([
                # html.Div([
                    head_map[header],
                ], style={'textAlign': 'center'}) 
        #     ])
        # ),
    # ])


def our_rangeslider(id, marks=None, min=0, max=1):
    
    # {str(year): str(year) for year in df['year'].unique() if year%2==0}
    return html.Div([
        # dbc.Card(
        #     dbc.CardBody([
        #         html.Div([
                                dcc.RangeSlider(
                                    # marks = None,
                                    marks=marks,
                                    min=min,
                                    max=max,
                                    step=None,
                                    value=[min, max],
                                    id=id,
                                ),], 
                                style={'margin-top': "30px"}
                            ) 
    #                     ])
    #     ),
    # ])



color_levels = ['#f2ebc7', '#ede5bb', "#e3dfb8"]




tab1_content = \
dbc.Card(
    dbc.CardBody([
# drawText(),

        dbc.Row([
            # drawText(),
            dbc.Col([
                html.Div(
                    drawText('Year', 5, color=color_levels[2]),
                    id='year'
                    ),
                dbc.Tooltip(
                    "Release Year of the track.",
                    target="year",
                    placement="bottom",
        ),
            ], width={"size": 6, "offset": 0}, ), 
            dbc.Col([
                our_rangeslider('year_selector', 
                # marks={str(year): str(year) for year in df['year'].unique() if year%8==0},
                min=df['year'].min(),
                max=df['year'].max(),
                )
            ], width={"size": 6, "offset": 0}),
            
            
        ], align='center',),
        html.Br(),
        dbc.Row([
            # drawText(),
            dbc.Col([
                html.Div(
                    drawText('Popularity', 5, color=color_levels[2]),
                    id='popularity'
                    ),
                dbc.Tooltip(
                    "A score from 0~1 to show how popular the song is.",
                    target="popularity",
                    placement="bottom",
                    )
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('popularity_selector', 
                # marks={str(year): str(year) for year in df['year'].unique() if year%8==0},
                max=1,
                )
            ], width={"size": 6, "offset": 0}),
            
            
        ], align='center',),
        html.Br(),
        dbc.Row([
            dbc.Col([
                
                html.Div(
                    drawText('Danceability', 5, color=color_levels[2]),
                    id='danceability'
                    ),
                dbc.Tooltip(
                    "A score from 0~1 to show how suitable a track is for dancing.",
                    target="danceability",
                    placement="bottom",
                    )
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('danceability_selector', 
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

        html.Br(),
        dbc.Row([
            dbc.Col([
                
                html.Div(
                    drawText('Genre', 5, color=color_levels[2]),
                    id='genre'
                    ),
                dbc.Tooltip(
                    "Genre of the track.",
                    target="genre",
                    placement="bottom",
                    )
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                html.Div(
                    dbc.Checklist(
                        options=[
                                {"label": 'Pop', "value": 'pop'}, 
                                {"label": 'Hip-hop', "value": 'hip hop'},
                                {"label": 'R&B', "value": 'R&B'}, 
                                {"label": 'Dance/Electronic', "value": 'Dance/Electronic'}, 
                                {"label": 'Rock', "value": 'rock'}, 
                                {"label": 'Metal', "value": 'metal'}, 
                                {"label": 'Latin', "value": 'latin'}, 
                                {"label": 'Others', "value": 'others'}, 
                                ],
                        value=['pop', 'hip hop', 'R&B', 'Dance/Electronic', 'rock', 'metal', 'latin'], 
                        id="genre-checklist", 
                        inline=True, 
                    ),
                    style={
                        # 'display': 'inline-block', 
                        'margin-left':'0px',
                        'font-size': '13px',
                    }                    
                ),
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

    ]), color=color_levels[1], className="mt-3",)

tab21_content = \
dbc.Card(
    dbc.CardBody([
# drawText(),

        dbc.Row([
            # drawText(),
            dbc.Col([
                
                html.Div(
                    drawText('Energy', 5, color=color_levels[2]),
                    id='energy'
                    ),
                dbc.Tooltip(
                    "A score from 0~1 to measure intensity and activity.",
                    target="energy",
                    placement="bottom",
                    )
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('energy_selector', 
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center'),

        html.Br(),
        dbc.Row([
            dbc.Col([
                html.Div(
                    drawText('Loudness', 5, color=color_levels[2]),
                    id='loudness'
                    ),
                dbc.Tooltip(
                    "The overall loudness of a track in decibels (dB)",
                    target="loudness",
                    placement="bottom",
                    )
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('loudness_selector', min=df['loudness'].min(), max=df['loudness'].max()
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

        html.Br(),
        dbc.Row([
            dbc.Col([
                

                html.Div(
                    drawText('Speechiness', 5, color=color_levels[2]),
                    id='speech'
                    ),
                dbc.Tooltip(
                    "Closer to 1.0 if more exclusively speech-like.",
                    target="speech",
                    placement="bottom",
                    )
                
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('speechiness_selector', 
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

        html.Br(),
        dbc.Row([
            dbc.Col([
                

                html.Div(
                    drawText('Acousticness', 5, color=color_levels[2]),
                    id='ac'
                    ),
                dbc.Tooltip(
                    "Closer to 1.0 if the track is more acoustic.",
                    target="ac",
                    placement="bottom",
                    )
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('acousticness_selector', 
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

    ]), color=color_levels[1], className="mt-3",)

tab22_content = \
dbc.Card(
    dbc.CardBody([
# drawText(),

        dbc.Row([
            # drawText(),
            dbc.Col([
                drawText('Instrumentalness', 5, color=color_levels[2])
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('instrumentalness_selector', 
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center'),

        html.Br(),
        dbc.Row([
            dbc.Col([
                drawText('Liveness', 5, color=color_levels[2])
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('liveness_selector', 
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

        html.Br(),
        dbc.Row([
            dbc.Col([
                drawText('Valence', 5, color=color_levels[2])
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('valence_selector', 
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

        html.Br(),
        dbc.Row([
            dbc.Col([
                drawText('Tempo', 5, color=color_levels[2])
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('tempo_selector', min=df['tempo'].min(), max=df['tempo'].max()
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

    ]), color=color_levels[1], className="mt-3",)

tabs2 = dbc.Tabs(
    [
        dbc.Tab(tab21_content, 
        label="Group 1", 
        tab_style={"margin-right": "0px", "padding": "1px"}, 
        # active_tab_style={"textTransform": "uppercase",}, 
        active_label_style={"background-color": color_levels[2]}
        ),

        dbc.Tab(tab22_content, 
        label="Group 2", 
        tab_style={"margin-right": "0px", "padding": "1px"}, 
        # active_tab_style={"textTransform": "uppercase",}, 
        active_label_style={"background-color": color_levels[2]}
        ),],style={"border": "1px solid #d1cbcb"},)

tab3_content = dbc.Card(
    dbc.CardBody(
        [

        dbc.Row([
            # drawText(),
            dbc.Col([
                drawText('Key', 5, color=color_levels[2])
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('key_selector', 
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center'),

        html.Br(),
        dbc.Row([
            dbc.Col([
                drawText('Duration', 5, color=color_levels[2])
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('duration_s_selector', 
                min=df['duration_s'].min(),
                max=df['duration_s'].max(),
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

        

        html.Br(),
        dbc.Row([
            dbc.Col([
                drawText('Mode', 5, color=color_levels[2])
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                html.Div(
                    dbc.Checklist(
                        options=[
                                {"label": '0', "value": 0}, 
                                {"label": '1', "value": 1}
                                ],
                        value=[0, 1], 
                        id="mode-checklist", 
                        inline=True, 
                    ),
                    style={'display': 'inline-block', 'margin-left':'30px'}                    
                ),
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

        html.Br(),
        dbc.Row([
            dbc.Col([
                drawText('Explicit', 5, color=color_levels[2])
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                html.Div(
                    [dbc.Checklist(
                        options=[
                            {"label": 'True', "value": 1}, 
                            {"label": 'False', "value": 0}
                            ], 
                        value=[1, 0], 
                        id="explicit-checklist", 
                        inline=True,
                        ),
                    ], 
                        style={'display': 'inline-block', 'margin-left':'30px'}
                    ),
            ], width={"size": 6, "offset": 0}),
        ], align='center',),

        ]
    ), color=color_levels[1], className="mt-3",)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, 
        label="Basics", 
        tab_style={"margin-right": "0px", "padding": "1px"}, 
        # active_tab_style={"textTransform": "uppercase",}, 
        active_label_style={"background-color": color_levels[2]}
        ),

        dbc.Tab(tabs2, 
        label="Advance", 
        tab_style={"margin-right": "0px", "padding": "1px"}, 
        # active_tab_style={"textTransform": "uppercase",}, 
        active_label_style={"background-color": color_levels[2]}
        ),

        dbc.Tab(tab3_content, 
        label="Others",
        tab_style={"margin-right": "0px", "padding": "1px"}, 
        # active_tab_style={"textTransform": "uppercase",}, 
        active_label_style={"background-color": color_levels[2]}
        ),
    ],
    style={"border": "2px solid #c9c8c1"},
)




app.layout = \
html.Div(
#     style={
# 'background-image': 'url("assets/bg1.jpg")',
# 'background-repeat': 'no-repeat',
# # 'background-position': 'right top',
# # 'background-size': '150px 100px'
# # "background-color": '#f2ebc7',
# },
    
    children=[
        dbc.Card(
        dbc.CardBody([
            dbc.Row(
                dbc.Col([
                    drawText("🔍Top Spotify Analysis🎸", color=color_levels[0]), 
                ],
                    width={"size": 9, "offset": 0}
                ),
                    align='center', justify="center",
                ),

            html.Br(),

            # dbc.CardGroup(
            #     style = {
            #         # "padding": "100px",
            #         "margin-top": "30px",
            #         "margin-left": "100px",
            #         "margin-right": "100px",
            #         # "margin-left": "100px",

            #         },
            #     children=[
                dbc.Row([
                    dbc.Col([
                        dbc.Card(
                                dbc.CardBody([
                        
                            tabs
                       
                                ]),
                                # style={"width": "33px"}
                                # style={
                                #     "width": "75%", 
                                #     "height": "50px",
                                #     "margin-left": "30px",
                                #     },
                                color=color_levels[1],
                        ),
                         ], 
                         width={"size": 4, "offset": 0},
                         style={"width": "25%","height": "50px"},
                         ), 

                
                    html.Br(),
                
                    dbc.Col([
                        dbc.Card(
                            dbc.CardBody([
                                # Title
                                dbc.Row(
                                    drawText("Characteristics Preview", header=4, color=color_levels[1]),
                                ),
                                # X
                                dbc.Row([
                                    dbc.Col(
                                        # html.Label(
                                        #     style={'textAlign': 'center'},
                                        #     children="Choose X-axis: ",
                                        # ), 
                                        
                                        # drawText("Choose X-axis", header=5, color=color_levels[1]),
                                        "Choose X-axis",
                                        style={'width': '50%', "margin-top": "15px", "margin-bottom": "10px", "textAlign": "center"}
                                    ),
                                # dbc.Row([
                                    dbc.Col([
                                        dcc.Dropdown(
                                            x_axis_choices,
                                            'danceability',
                                            id='xaxis-column',
                                            style={"background-color": "#f5f1d3"}
                                            ),
                                        ], 
                                align='center', 
                                        style={
                                            'width': '50%', 
                                            # 'display': 'inline-block', 
                                            # 'marginTop' : '60px',
                                            "margin-top": "10px", "margin-bottom": "10px", 
                                            }
                                        ),
                            ]),
                                # Y
                                dbc.Row([
                                    dbc.Col(
                                        # html.Label(
                                        #     style={'textAlign': 'center'},
                                        #     children="Choose X-axis: ",
                                        # ), 
                                        # drawText("Choose Y-axis", header=5, color=color_levels[1]),
                                        "Choose Y-axis",
                                        style={'width': '50%', "margin-top": "15px", "margin-bottom": "10px", "textAlign": "center"}
                                    ),
                                # dbc.Row([
                                    dbc.Col([
                                        dcc.Dropdown(
                                            y_axis_choices,
                                            'popularity',
                                            id='yaxis-column',
                                            style={"background-color": "#f5f1d3"}
                                            ),
                                        ], 
                                align='center', 
                                        style={
                                            'width': '50%', 
                                            # 'display': 'inline-block', 
                                            # 'marginTop' : '60px',
                                            "margin-top": "10px", "margin-bottom": "10px", 
                                            }
                                        ),
                            ]),
                                
                                # html.Br(),
                                dbc.Row([
                                    dcc.Graph(id='indicator-graphic'),
                                ], align='center'),
                        ]), color=color_levels[1])
                    ], 
                    width={"size": 4, "offset": 0},
                    style={"width": "36%","height": "50px"}
                    ), 

                    dbc.Col([
                        dbc.Card(
                            dbc.CardBody([
                                
                                # Title
                                dbc.Row(
                                    drawText("Advanced Analysis", header=4, color=color_levels[1]),
                                ),
                                dbc.Row([
                                    dbc.Col(
                                        "Find an Advanced Chart:",
                                        style={'width': '50%', "margin-top": "15px", "margin-bottom": "10px", "textAlign": "center"}
                                    ),
                                # dbc.Row([
                                    dbc.Col([
                                        dcc.Dropdown(
                                            advanced_chart_titles,
                                            'Treemap',
                                            id='advanced_charts',
                                            style={"background-color": "#f5f1d3"}
                                            ),
                                        ], 
                                align='center', 
                                        style={
                                            'width': '50%', 
                                            # 'display': 'inline-block', 
                                            # 'marginTop' : '60px',
                                            "margin-top": "10px", "margin-bottom": "10px", 
                                            }
                                        ),
                            ]),
                                
                                dbc.Row([
                                    dcc.Graph(id='sub-graphic'),
                                ], align='center'),
                        ]), color=color_levels[1])
                    ], 
                    width={"size": 4, "offset": 0},
                    style={"width": "36%","height": "50px"}
                    ), 
            ], 
           align='center', justify="center",
           ),     
        ]), 
        color = color_levels[0],
        style={"height": "150vh"}
    ),
    ],
)

# app.layout = html.Div(children=[
#     html.H1('Hello Dash', style={'background-image': 'url(assets/bg.webp)'})
#     ])

@app.callback(
    # Output
    Output('indicator-graphic', 'figure'),
    Output('sub-graphic', 'figure'),

    # Axis features
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    # Input('xaxis-type', 'value'),
    # Input('yaxis-type', 'value'),
    # Input('year--slider', 'value'),

    # Range selectors
    [Input('duration_s_selector', 'value')],
    [Input('year_selector', 'value')],
    [Input('popularity_selector', 'value')],
    [Input('danceability_selector', 'value')],
    [Input('energy_selector', 'value')],
    [Input('key_selector', 'value')],
    [Input('loudness_selector', 'value')],
    [Input('speechiness_selector', 'value')],
    [Input('acousticness_selector', 'value')],
    [Input('instrumentalness_selector', 'value')],
    [Input('liveness_selector', 'value')],
    [Input('valence_selector', 'value')],
    [Input('tempo_selector', 'value')],

    [Input("explicit-checklist", "value")],
    [Input("mode-checklist", "value")],
    [Input("genre-checklist", "value")],

    # Input('button_1', 'n_clicks')
    Input('advanced_charts', 'value'),

    Input('indicator-graphic', 'selectedData'),
    
)

def update_graph(xaxis_column_name, yaxis_column_name,
                #  xaxis_type, yaxis_type,
                #  year_value,
                duration_s_range,
                year_range,
                popularity_range,
                danceability_range,
                energy_range,
                key_range,
                loudness_range,
                speechiness_range,
                acousticness_range,
                instrumentalness_range,
                liveness_range,
                valence_range,
                tempo_range,
                explicit_checklist,
                mode_checklist,
                genre_checklist,

                # button_1,
                advanced_charts,
                selectedData,
                 ):

    # dff = df[df['year'] <= year_value]
    dff = df.copy()
    dff = dff[dff['duration_s'].between(duration_s_range[0], duration_s_range[1], inclusive='both')]
    dff = dff[dff['year'].between(year_range[0], year_range[1], inclusive='both')]
    dff = dff[dff['duration_s'].between(duration_s_range[0], duration_s_range[1], inclusive='both')]
    dff = dff[dff['year'].between(year_range[0], year_range[1], inclusive='both')]
    dff = dff[dff['popularity'].between(popularity_range[0], popularity_range[1], inclusive='both')]
    dff = dff[dff['danceability'].between(danceability_range[0], danceability_range[1], inclusive='both')]
    dff = dff[dff['energy'].between(energy_range[0], energy_range[1], inclusive='both')]
    dff = dff[dff['key'].between(key_range[0], key_range[1], inclusive='both')]
    dff = dff[dff['loudness'].between(loudness_range[0], loudness_range[1], inclusive='both')]
    dff = dff[dff['speechiness'].between(speechiness_range[0], speechiness_range[1], inclusive='both')]
    dff = dff[dff['acousticness'].between(acousticness_range[0], acousticness_range[1], inclusive='both')]
    dff = dff[dff['instrumentalness'].between(instrumentalness_range[0], instrumentalness_range[1], inclusive='both')]
    dff = dff[dff['liveness'].between(liveness_range[0], liveness_range[1], inclusive='both')]
    dff = dff[dff['valence'].between(valence_range[0], valence_range[1], inclusive='both')]
    dff = dff[dff['tempo'].between(tempo_range[0], tempo_range[1], inclusive='both')]
    dff = dff.loc[dff['explicit'].isin(list(explicit_checklist))]
    dff = dff.loc[dff['mode'].isin(list(mode_checklist))]
    
    others = ['country', 'Folk/Acoustic', 'World/Traditional', 'easy listening', 'jazz', 'classical']
    if 'others' in genre_checklist:
        genre_checklist.remove('others')
        genre_checklist.extend(others)
    
    dff = dff.loc[dff[genre_checklist].isin([1]).any(axis=1)]
    # print(len(dff))
    if dff.empty:
        return px.scatter(), px.scatter()

    fig1 = px.scatter(dff, x=dff[xaxis_column_name],
                     y=dff[yaxis_column_name],
                     hover_name=dff['song'], 
                    #  hover_data=[df['popularity'], df['danceability']],
                    hover_data={

                        'artist': True,
                        'popularity': True, 
                        'danceability': True,
                        'genre': True,
                        
                        },
                    color='popularity',
                    color_continuous_scale='deep',
                     )

    fig1.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, 
                    hovermode='closest', 
                    height=500, 
                    width=480,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
    )

    fig1.update_xaxes(title=xaxis_column_name.capitalize(),showgrid=False)
                    #  type='linear' if xaxis_type == 'Linear' else 'log')

    fig1.update_yaxes(title=yaxis_column_name.capitalize(),showgrid=False)
                    #  type='linear' if yaxis_type == 'Linear' else 'log')

    # advanced_chart_titles = 
    # ['paiwise correlation', 
    # 'treemap', 
    # 'genre statistics', 
    # 'best singers', 
    # 'feature distribution']


    # selected_points = dff.index
    # if selectedData and selectedData['points']:
    #     selected_points = np.intersect1d(selected_points,
    #             [p['customdata'] for p in selectedData['points']])
    # print(selected_points)
    
    # fig1.update_traces(selectedpoints=selected_points,
    #                   customdata=dff.index,
    #                   mode='markers+text', unselected={'marker': { 'opacity': 0.3 }, 'textfont': { 'color': 'rgba(0, 0, 0, 0)' } })
        
    dfff = dff.copy()
    # print(dfff.index)
    # dfff = dfff.loc[selected_points]
    fig2_w = 480
    fig2_h = 480
    fig2 = px.scatter()
    if advanced_charts == advanced_chart_titles[0]:
        
        fig2=px.imshow(dfff[x_axis_choices].corr(),text_auto='.2f',color_continuous_scale=px.colors.sequential.Pinkyl,aspect='auto',title='<b>Pairwise Correlation')
        fig2.update_layout(title_x=0.5, height=fig2_h,width=fig2_w,paper_bgcolor='rgba(0,0,0,0)',margin=dict(l=0, r=20, t=30, b=0),)
        fig2.update_xaxes(showticklabels = False,)
        fig2.update_yaxes(showticklabels = False,)
    elif advanced_charts == advanced_chart_titles[1]:
        max_value_count = max(dfff['artist'].value_counts())
        m = dfff['artist'].value_counts()>=0.5 * max_value_count
        m = m.to_frame()
        m = m[m['artist']==True].to_dict()
        m = m.values()
        m = list(m)
        m = list(m[0].keys())
        fig2=px.treemap(dfff[dfff['artist'].isin(m)], path=[px.Constant('Singer'),'artist','genre','song'],values='popularity',title='<b>TreeMap of Singers')
        fig2.update_traces(root_color='lightgreen')
        fig2.update_layout(title_x=0.5, height=fig2_h,width=fig2_w,paper_bgcolor='rgba(0,0,0,0)',margin=dict(l=0, r=20, t=30, b=0),)
    elif advanced_charts == advanced_chart_titles[2]:
        # fig2 = go.Figure(data=[go.Bar(x=genre_counts.keys(), y=genre_counts.values(), title="Total Songs by Genre", marker_color='rgb(158,202,225)')])
        # fig2=px.bar(x=genre_counts.keys(), y=genre_counts.values(), title="<b>Total Songs by Genre")
        fig2=px.bar(x=genre_checklist, y=list(dfff[genre_checklist].sum()), title="<b>Total Songs by Genre")
        fig2.update_xaxes(title='genre'.capitalize(),)
        fig2.update_yaxes(title='counts of songs'.capitalize(),)
        fig2.update_layout(title_x=0.5, height=fig2_h,width=fig2_w,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',margin=dict(l=20, r=20, t=30, b=0),)
        fig2.update_traces(marker_color="#55e6e6")
    # if 'button_1' == ctx.triggered_id:
        # fig2 = fig1
    elif advanced_charts == advanced_chart_titles[3]:
        pop_scores = []
        for genre in genre_checklist:
            pop_scores.append(round(dfff.loc[dfff[[genre]].isin([1]).any(axis=1)]['popularity'].sum(), 2))
        fig2=px.bar(x=genre_checklist, y=pop_scores, title="<b>Popularity Score by Genre")
        fig2.update_xaxes(title='genre'.capitalize(),)
        fig2.update_yaxes(title='popularity score sum'.capitalize(),)
        fig2.update_layout(title_x=0.5, height=fig2_h,width=fig2_w,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',margin=dict(l=20, r=20, t=30, b=0),)
        fig2.update_traces(marker_color="#157894")
    elif advanced_charts == advanced_chart_titles[4]:
        classes = ['valence','speechiness','energy','danceability']
        fig2 = px.scatter_matrix(dfff, dimensions = classes, title="<b>Scatterplot Matrix",color ="popularity",size_max = 0.1, )
        fig2.update_traces(diagonal_visible=False)
        fig2.update_traces(marker_size = 4)
        # fig2.update_coloraxes(showscale=False)
        # fig2.update_xaxes(showticklabels = [False]*5,showgrid=[False]*5)
        # fig2.update_yaxes(showticklabels = [False]*5,showgrid=[False]*5)
        fig2.update_layout({"xaxis"+str(i+1): dict(showgrid = True, showticklabels=False) for i in range(len(classes))})
        fig2.update_layout({"yaxis"+str(i+1): dict(showgrid = True, showticklabels=False) for i in range(len(classes))})
        fig2.update_layout(title_x=0.5, height=fig2_h,width=470,paper_bgcolor='#e1eded',plot_bgcolor="#7bcae0",margin=dict(l=20, r=0, t=50, b=40),)

    elif advanced_charts == advanced_chart_titles[5]:
        fig2=ps.make_subplots(rows=3,cols=3,subplot_titles=('Popularity', 'Danceability', 'Energy', 'Loudness', 'Speechiness', 'Acousticness', 'Liveness', 'Valence', 'Tempo'))
        fig2.add_trace(go.Histogram(x=dfff['popularity'],name='popularity'),row=1,col=1)
        fig2.add_trace(go.Histogram(x=dfff['danceability'],name='danceability'),row=1,col=2)
        fig2.add_trace(go.Histogram(x=dfff['energy'],name='energy'),row=1,col=3)
        fig2.add_trace(go.Histogram(x=dfff['loudness'],name='loudness'),row=2,col=1)
        fig2.add_trace(go.Histogram(x=dfff['speechiness'],name='speechiness'),row=2,col=2)
        fig2.add_trace(go.Histogram(x=dfff['acousticness'],name='acousticness'),row=2,col=3)
        fig2.add_trace(go.Histogram(x=dfff['liveness'],name='liveness'),row=3,col=1)
        fig2.add_trace(go.Histogram(x=dfff['valence'],name='valence'),row=3,col=2)
        fig2.add_trace(go.Histogram(x=dfff['tempo'],name='tempo'),row=3,col=3)
        # fig2.update_layout(height=900,width=900,title_text='<b>Feature Distribution')
        fig2.update_layout(title_text='<b>Feature Distribution', title_x=0.5, height=fig2_h,width=fig2_w,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',margin=dict(l=20, r=20, t=90, b=0),showlegend=False)

    return fig1, fig2

# @app.callback(
#     # Output
#     Output('sub-graphic', 'figure'),

#     # Input
#     Input('button_1', 'n_clicks'),

# )

# def update_multiple_images(button_1):

#     fig2 = px.scatter()

#     if 'button_1' == ctx.triggered_id:
#         fig2 = px.scatter(dff2, x=dff2['year'],
#                      y=dff2['popularity'],)
#     return fig2



if __name__ == '__main__':
    app.run_server(debug=True, port=8098)