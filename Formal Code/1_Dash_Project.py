from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('Datasets/Clean_Dataset.csv')

continues_attributes = ['duration_ms', 'year',
       'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo']
categorical_attributes = ['artist', 'song', 'explicit', 'genre']



app.layout = \
html.Div([
    
    # Right part
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
                        'width': '65%', 
                        # 'display': 'inline-block', 
                        # 'marginTop' : '60px',
                        })
            ]),
            html.Div([
            "Choose Y-axis column: ",
            dcc.Dropdown(
                continues_attributes,
                'popularity',
                id='yaxis-column'
            ),
            ]
            # , style={'display': 'inline-block'}
            ),

            html.Div([
                html.Div([
                    html.Label('Choose X-axis type: ', style={'display': 'inline-block'}),
                    html.Div(dcc.RadioItems(
                        ['Linear', 'Log'],
                        'Linear',
                        id='xaxis-type',
                        inline=True
                    ), style={'display': 'inline-block'})
                ]),
            ]),
            html.Div([
                html.Div([
                    html.Label('Choose Y-axis type: ', style={'display': 'inline-block'}),
                    html.Div(dcc.RadioItems(
                        ['Linear', 'Log'],
                        'Linear',
                        id='yaxis-type',
                        inline=True
                    ), style={'display': 'inline-block'})
                ]),
            ]),
        ],         
        style={'width': '65%', 'display': 'inline-block', 'float': 'right'},
    ),

        # Graph
        html.Div([
            dcc.Graph(id='indicator-graphic'),
            ], 
            # style for graph
            style={'width': '65%', 'display': 'inline-block', 'float': 'right'},
        ),

    ]),
    
    # Left part
    html.Div([

        # Parameters
        html.Div([
            
            # Range sliders
            html.Div([
                'Duration (ms)',
                dcc.RangeSlider(
                    min=df['duration_ms'].min(),
                    max=df['duration_ms'].max(),
                    step=None,
                    value=[df['duration_ms'].min(), df['duration_ms'].max()],
                    id='duration_ms_selector',
                ),
                'Year',
                dcc.RangeSlider(
                    min=df['year'].min(),
                    max=df['year'].max(),
                    step=None,
                    value=[df['year'].min(), df['year'].max()],
                    id='year_selector',
                    marks={str(year): str(year) for year in df['year'].unique() if year%2==0},
                ),
                'Popularity',
                dcc.RangeSlider(
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
                    min=df['danceability'].min(),
                    max=df['danceability'].max(),
                    step=None,
                    value=[df['danceability'].min(),
                    df['danceability'].max()],
                    id='danceability_selector',
                ),
                'Energy',
                dcc.RangeSlider(
                    min=df['energy'].min(),
                    max=df['energy'].max(),
                    step=None,
                    value=[df['energy'].min(),
                    df['energy'].max()],
                    id='energy_selector',
                ),
                'Key',
                dcc.RangeSlider(
                    min=df['key'].min(),
                    max=df['key'].max(),
                    step=None,
                    value=[df['key'].min(),
                    df['key'].max()],
                    id='key_selector',
                ),
                'Loudness',
                dcc.RangeSlider(
                    min=df['loudness'].min(),
                    max=df['loudness'].max(),
                    step=None,
                    value=[df['loudness'].min(),
                    df['loudness'].max()],
                    id='loudness_selector',
                ),
                'Speechiness',
                dcc.RangeSlider(
                    min=df['speechiness'].min(),
                    max=df['speechiness'].max(),
                    step=None,
                    value=[df['speechiness'].min(),
                    df['speechiness'].max()],
                    id='speechiness_selector',
                ),
                'Acousticness',
                dcc.RangeSlider(
                    min=df['acousticness'].min(),
                    max=df['acousticness'].max(),
                    step=None,
                    value=[df['acousticness'].min(),
                    df['acousticness'].max()],
                    id='acousticness_selector',
                ),
                'Instrumentalness',
                dcc.RangeSlider(
                    min=df['instrumentalness'].min(),
                    max=df['instrumentalness'].max(),
                    step=None,
                    value=[df['instrumentalness'].min(),
                    df['instrumentalness'].max()],
                    id='instrumentalness_selector',
                ),
                'Liveness',
                dcc.RangeSlider(
                    min=df['liveness'].min(),
                    max=df['liveness'].max(),
                    step=None,
                    value=[df['liveness'].min(),
                    df['liveness'].max()],
                    id='liveness_selector',
                ),
                'Valence',
                dcc.RangeSlider(
                    min=df['valence'].min(),
                    max=df['valence'].max(),
                    step=None,
                    value=[df['valence'].min(),
                    df['valence'].max()],
                    id='valence_selector',
                ),
                'Tempo',
                dcc.RangeSlider(
                    min=df['tempo'].min(),
                    max=df['tempo'].max(),
                    step=None,
                    value=[df['tempo'].min(),
                    df['tempo'].max()],
                    id='tempo_selector',
                ),
            ],),

     
            html.Div([
                html.Label(['Explicit'], style={'display': 'inline-block'}),
                html.Div([dcc.Checklist(['True', 'False'], ['True', 'False'], id="explicit-checklist", inline=True)], style={'display': 'inline-block', 'margin-left':'30px'}),
                html.Br(),
                html.Label(['Mode'], style={'display': 'inline-block'}),
                dcc.Checklist(['0', '1'], ['0', '1'], id="mode-checklist", inline=True, style={'display': 'inline-block', 'margin-left':'30px'}),
                ####################
                #### TODO ##########
                ####################
                # Genre,
                # dcc.Checklist([''], [], id="genre-checklist", inline=True),
            ]),
        ], 
        # style for all parameters
        style={'width': '31%',}
        ),
        
        
    ]),
    
    
    
    

    

])


@app.callback(
    # Output
    Output('indicator-graphic', 'figure'),

    # Axis features
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
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
    
)
    
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
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


    fig = px.scatter(dff, x=dff[xaxis_column_name],
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

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)