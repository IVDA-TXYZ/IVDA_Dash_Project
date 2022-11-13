from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('Formal Code/Datasets/Clean_Dataset.csv')

continues_attributes = ['duration_ms', 'year',
       'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo']
categorical_attributes = ['artist', 'song', 'explicit', 'genre']



app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                continues_attributes,
                'year',
                id='xaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='xaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                continues_attributes,
                'popularity',
                id='yaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='yaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    # dcc.Slider(
    #     df['year'].min(),
    #     df['year'].max(),
    #     step=None,
    #     id='year--slider',
    #     value=df['year'].max(),
    #     marks={str(year): str(year) for year in df['year'].unique()},

    # )
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    # Input('year--slider', 'value')
    )
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                #  year_value
                 ):

    # dff = df[df['year'] <= year_value]
    dff = df

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
                     )

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    # range selector

    # fig.update_layout(
    # xaxis=dict(
    #     rangeselector=dict(
    #         buttons=list([
    #             dict(step="all")
    #         ])
    #     ),
    #     rangeslider=dict(
    #         visible=True
    #     ),
    #     type="date"
    #     )
    # )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)