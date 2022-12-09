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
            ]), color=color
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
                                ),], style={'margin-top': "30px"}
                            ) 
    #                     ])
    #     ),
    # ])

color_text_slider = "#e3dfb8"





tab1_content = \
dbc.Card(
    dbc.CardBody([
# drawText(),

        dbc.Row([
            # drawText(),
            dbc.Col([
                drawText('Year (2000-2020)', 5, color=color_text_slider)
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('year_selector', 
                # marks={str(year): str(year) for year in df['year'].unique() if year%8==0},
                min=df['year'].min(),
                max=df['year'].max(),
                )
            ], width={"size": 6, "offset": 0}),
            
            
        ], align='center'),
        html.Br(),
        dbc.Row([
            # drawText(),
            dbc.Col([
                drawText('Popularity', 5, color=color_text_slider)
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('popularity_selector', 
                # marks={str(year): str(year) for year in df['year'].unique() if year%8==0},
                max=100,
                )
            ], width={"size": 6, "offset": 0}),
            
            
        ], align='center'),
        html.Br(),
        dbc.Row([
            drawText(), 
        ], align='center'),

    ]), color='#ede5bb', className="mt-3",)

tab2_content = \
dbc.Card(
    dbc.CardBody([
# drawText(),

        dbc.Row([
            # drawText(),
            dbc.Col([
                drawText('Energy', 5, color=color_text_slider)
            ], width={"size": 6, "offset": 0},), 
            dbc.Col([
                our_rangeslider('energy_selector', 
                )
            ], width={"size": 6, "offset": 0}),
        ], align='center'),
        html.Br(),
        dbc.Row([
            drawText(), 
        ], align='center'),
        html.Br(),
        dbc.Row([
            drawText(), 
        ], align='center'),

    ]), color='#ede5bb', className="mt-3",)

tab3_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 3!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]
    ),
    className="mt-3",
)

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Basic Features"),
        dbc.Tab(tab2_content, label="Advanced Features"),
        dbc.Tab(tab3_content, label="Others"),
    ]
)




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
            dbc.Row(
                dbc.Col([
                    drawText("🔍Search songs🎸"), 
                ],
                    width={"size": 9, "offset": 0}
                ),
                    align='center', justify="center",
                ),

            html.Br(),

            dbc.Row([

             dbc.Col([
                tabs
            ], width={"size": 5, "offset": 0}), 

            
            html.Br(),
           
            dbc.Col([
                dbc.Card(
                    dbc.CardBody([
                # drawText(),

                dbc.Row([
                    drawText(), 
                ], align='center'),
                html.Br(),
                dbc.Row([
                    drawText(), 
                ], align='center'),
                 ]), color='#ede5bb')
            ], width={"size": 5, "offset": 0}), 
           ], align='center', justify="center",),     
        ]), 
        color = '#f2ebc7'
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
    app.run_server(debug=True, port=8098)