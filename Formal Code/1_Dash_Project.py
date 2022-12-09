from dash import Dash, dcc, html, Input, Output, ctx
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# load_figure_template('CERULEAN')

df = pd.read_csv('Datasets/Clean_Dataset.csv')

dff2 = pd.read_csv('Datasets/Clean_Dataset.csv')

continues_attributes = ['duration_ms', 'year',
       'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo']
categorical_attributes = ['artist', 'song', 'explicit', 'genre']
advanced_chart_titles = ['paiwise correlation', 'treemap', 'genre statistics', 'best singers', 'feature distribution']

import pickle
with open('Datasets/count_list.pickle', 'rb') as handle:
    genre_counts = pickle.load(handle)

app.layout = \
html.Div(
    style={
'background-image': 'url("assets/bg1.jpg")',
'background-repeat': 'no-repeat',
# 'background-position': 'right top',
# 'background-size': '150px 100px'
},
    
    children=[
        dbc.Card(
            dbc.CardBody([
    
    # Right part
    dbc.Col([
    html.Div([
        # Axes
        html.Div([
            html.Div([
                html.Label("Choose X-axis column: ", 
                # style={'display': 'inline-block', 'font' : '60px',},
                ),
                html.Div(
                    dcc.Dropdown(
                    continues_attributes,
                    'year',
                    id='xaxis-column'
                    ),
                    style={
                        'width': '50%', 
                        # 'display': 'inline-block', 
                        # 'marginTop' : '60px',
                        })
            ]),
            html.Div([
            "Choose Y-axis column: ",
            html.Div(
            dcc.Dropdown(
                continues_attributes,
                'popularity',
                id='yaxis-column'
            ),
            style={
                        'width': '50%', 
                        # 'display': 'inline-block', 
                        # 'marginTop' : '60px',
                        },),
            ]
            # , style={'display': 'inline-block'}
            ),
        
            # html.Div([
            #     html.Div([
            #         html.Label('Choose X-axis type: ', style={'display': 'inline-block'}),
            #         html.Div(dcc.RadioItems(
            #             ['Linear', 'Log'],
            #             'Linear',
            #             id='xaxis-type',
            #             inline=True
            #         ), style={'display': 'inline-block'})
            #     ]),
            # ]),
            # html.Div([
            #     html.Div([
            #         html.Label('Choose Y-axis type: ', style={'display': 'inline-block'}),
            #         html.Div(dcc.RadioItems(
            #             ['Linear', 'Log'],
            #             'Linear',
            #             id='yaxis-type',
            #             inline=True
            #         ), style={'display': 'inline-block'})
            #     ]),
            # ]),
        
            html.Br(),
        ],         
        style={'width': '62%', 'display': 'inline-block', 'float': 'right'},
    ),

        # Graph 1
        html.Div([
            dcc.Graph(id='indicator-graphic'),
            ], 
            # style for graph
            style={'width': '65%', 'display': 'inline-block', 'float': 'right'},
        ),

        # html.Hr(style={'width': '63%', 'display': 'inline-block', 'float': 'right'}),

        # html.Div([
        #     html.Div(
        #     html.Button('Button 1', id='button_1', n_clicks=0, style={'display': 'inline-block',},),
        #     className='col',), 
        #     html.Div(
        #         html.Button('Button 2', id='button_2', n_clicks=0, style={'display': 'inline-block',},),
        #     className='col',),
        # ], 
        #     style={'float': 'right', 'vertical-align': 'bottom',}, 
        #     className='row',
        #     ),

        
        html.Div([html.Br(),
                html.Label("Find an advanced chart: ", 
                # style={'display': 'inline-block', 'font' : '60px',},
                ),
                html.Div(
                    dcc.Dropdown(
                        advanced_chart_titles,
                    'treemap',
                    id='advanced_charts'
                    ),
                    style={
                        'width': '50%', 
                        # 'display': 'inline-block', 
                        # 'marginTop' : '60px',
                        })
            ], style={'width': '62%', 'display': 'inline-block', 'float': 'right'},),

        
        # Graph 2
        html.Div([
            dcc.Graph(id='sub-graphic'),
            ], 
            # style for graph
            style={'width': '65%', 'display': 'inline-block', 'float': 'right'}, 
            className='row',
        ),
        
        

    ], 

    # style for all parameters
    # style={"margin-top":"30px", "margin-right":"10px"},
    className='cotainer',

    ),
    ], width=3),
    # Left part
    dbc.Col([
    html.Div([

        # Parameters
        html.Div([
            
            html.H1("🔍Search songs🎸",style = {"text-align":"center","margin-top":"10px"}),
            # Range sliders
            html.Div(
                [
                    dbc.Row([
                'Year',
                dcc.RangeSlider(
                    # marks = None,
                    marks={str(year): str(year) for year in df['year'].unique() if year%2==0},
                    min=df['year'].min(),
                    max=df['year'].max(),
                    step=None,
                    value=[df['year'].min(), df['year'].max()],
                    id='year_selector',
                ),
                    ]),

                    dbc.Row([
                'Duration',
                dcc.RangeSlider(
                    marks = None,
                    min=df['duration_ms'].min(),
                    max=df['duration_ms'].max(),
                    step=None,
                    value=[df['duration_ms'].min(), df['duration_ms'].max()],
                    id='duration_ms_selector',
                ),
                ]),
                
                'Popularity',
                dcc.RangeSlider(
                    marks = None,
                    # min=df['popularity'].min(),
                    # max=df['popularity'].max(),
                    min=0,
                    max=100,
                    step=None,
                    # value=[df['popularity'].min(),
                    # df['popularity'].max()],
                    value=[0, 100],
                    id='popularity_selector',
                ),
                'Danceability',
                dcc.RangeSlider(
                    marks = None,
                    min=df['danceability'].min(),
                    max=df['danceability'].max(),
                    step=None,
                    value=[df['danceability'].min(),
                    df['danceability'].max()],
                    id='danceability_selector',
                ),
                'Energy',
                dcc.RangeSlider(
                    marks = None,
                    min=df['energy'].min(),
                    max=df['energy'].max(),
                    step=None,
                    value=[df['energy'].min(),
                    df['energy'].max()],
                    id='energy_selector',
                ),
                'Key',
                dcc.RangeSlider(
                    marks = None,
                    min=df['key'].min(),
                    max=df['key'].max(),
                    step=None,
                    value=[df['key'].min(),
                    df['key'].max()],
                    id='key_selector',
                ),
                'Loudness',
                dcc.RangeSlider(
                    marks = None,
                    min=df['loudness'].min(),
                    max=df['loudness'].max(),
                    step=None,
                    value=[df['loudness'].min(),
                    df['loudness'].max()],
                    id='loudness_selector',
                ),
                'Speechiness',
                dcc.RangeSlider(
                    marks = None,
                    min=df['speechiness'].min(),
                    max=df['speechiness'].max(),
                    step=None,
                    value=[df['speechiness'].min(),
                    df['speechiness'].max()],
                    id='speechiness_selector',
                ),
                'Acousticness',
                dcc.RangeSlider(
                    marks = None,
                    min=df['acousticness'].min(),
                    max=df['acousticness'].max(),
                    step=None,
                    value=[df['acousticness'].min(),
                    df['acousticness'].max()],
                    id='acousticness_selector',
                ),
                'Instrumentalness',
                dcc.RangeSlider(
                    marks = None,
                    min=df['instrumentalness'].min(),
                    max=df['instrumentalness'].max(),
                    step=None,
                    value=[df['instrumentalness'].min(),
                    df['instrumentalness'].max()],
                    id='instrumentalness_selector',
                ),
                'Liveness',
                dcc.RangeSlider(
                    marks = None,
                    min=df['liveness'].min(),
                    max=df['liveness'].max(),
                    step=None,
                    value=[df['liveness'].min(),
                    df['liveness'].max()],
                    id='liveness_selector',
                ),
                'Valence',
                dcc.RangeSlider(
                    marks = None,
                    min=df['valence'].min(),
                    max=df['valence'].max(),
                    step=None,
                    value=[df['valence'].min(),
                    df['valence'].max()],
                    id='valence_selector',
                ),
                'Tempo',
                dcc.RangeSlider(
                    marks = None,
                    min=df['tempo'].min(),
                    max=df['tempo'].max(),
                    step=None,
                    value=[df['tempo'].min(),
                    df['tempo'].max()],
                    id='tempo_selector',
                ),
            ],style={}
            ),

     
            html.Div([
                html.Label(['Explicit'], style={'display': 'inline-block'}),
                html.Div([dcc.Checklist(options=[{"label": 'True', "value": 1}, {"label": 'False', "value": 0}], value=[1, 0], id="explicit-checklist", inline=True)], style={'display': 'inline-block', 'margin-left':'30px'}),
                html.Br(),
                html.Label(['Mode'], style={'display': 'inline-block'}),
                dcc.Checklist([0, 1], [0, 1], id="mode-checklist", inline=True, style={'display': 'inline-block', 'margin-left':'30px'}),
                ####################
                #### TODO ##########
                ####################
                # Genre,
                # dcc.Checklist([''], [], id="genre-checklist", inline=True),
            ]),
        ], 
        # style for all parameters
        style={'width': '31%',"margin":"10px"}
        ),
        
        
    ]),
    ]),
    
    
    

    
        ]),),
])

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
    [Input('duration_ms_selector', 'value')],
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

    # Input('button_1', 'n_clicks')
    Input('advanced_charts', 'value')
    
)

def update_graph(xaxis_column_name, yaxis_column_name,
                #  xaxis_type, yaxis_type,
                #  year_value,
                duration_ms_range,
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

                # button_1,
                advanced_charts,
                 ):

    # dff = df[df['year'] <= year_value]
    dff = df.copy()
    dff = dff[dff['duration_ms'].between(duration_ms_range[0], duration_ms_range[1], inclusive='both')]
    dff = dff[dff['year'].between(year_range[0], year_range[1], inclusive='both')]
    dff = dff[dff['duration_ms'].between(duration_ms_range[0], duration_ms_range[1], inclusive='both')]
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
                        
                        },
                    color='popularity',
                    color_continuous_scale='deep',
                     )

    fig1.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig1.update_xaxes(title=xaxis_column_name,)
                    #  type='linear' if xaxis_type == 'Linear' else 'log')

    fig1.update_yaxes(title=yaxis_column_name,)
                    #  type='linear' if yaxis_type == 'Linear' else 'log')

    # advanced_chart_titles = 
    # ['paiwise correlation', 
    # 'treemap', 
    # 'genre statistics', 
    # 'best singers', 
    # 'feature distribution']


    fig2 = px.scatter()
    if advanced_charts == advanced_chart_titles[0]:
        fig2=px.imshow(dff.corr(),text_auto=True,color_continuous_scale=px.colors.sequential.Pinkyl,aspect='auto',title='<b>Paiwise Correlation')
        fig2.update_layout(title_x=0.5, height=800,width=800,)
    elif advanced_charts == advanced_chart_titles[1]:
        max_value_count = max(dff['artist'].value_counts())
        m = dff['artist'].value_counts()>=0.5 * max_value_count
        m = m.to_frame()
        m = m[m['artist']==True].to_dict()
        m = m.values()
        m = list(m)
        m = list(m[0].keys())
        dff = dff[dff['artist'].isin(m)]
        fig2=px.treemap(dff, path=[px.Constant('Singer'),'artist','genre','song'],values='popularity',title='<b>TreeMap of Singers')
        fig2.update_traces(root_color='lightgreen')
        fig2.update_layout(title_x=0.5, width = 800, height = 800)
    elif advanced_charts == advanced_chart_titles[2]:
        # fig2 = go.Figure(data=[go.Bar(x=genre_counts.keys(), y=genre_counts.values(), title="Genre Statistics", marker_color='rgb(158,202,225)')])
        fig2=px.bar(x=genre_counts.keys(), y=genre_counts.values(), title="<b>Genre Statistics")
        fig2.update_xaxes(title='genre',)
        fig2.update_yaxes(title='counts of songs',)
        fig2.update_layout(title_x=0.5, width = 800, height = 500,)

    # if 'button_1' == ctx.triggered_id:
        # fig2 = fig1
    

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
    app.run_server(debug=True)