import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
import requests
import json


# Initialize the app
app = dash.Dash(__name__)
#app.config.suppress_callback_exceptions = True




# helpful funtions to create table data
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ],style={'width':'100%', 'margin':25, 'textAlign': 'center'})


# url = 'https://rest.coinapi.io/v1/ohlcv/BTC/USD/latest?period_id=10DAY'
#     #apikey = '6B081E29-633F-4CDD-9743-9219FBE0709B'
# apikey='60F4A03A-174B-4FC1-973D-D05364E6AEEB'
#     #60F4A03A-174B-4FC1-973D-D05364E6AEEB
# headers = {'X-CoinAPI-Key': apikey}
# response = requests.get(url, headers=headers)
# data = json.loads(response.text)
# df = pd.DataFrame(data)





app.layout = html.Div(
    children=[

        html.Div(className='row',children=[

        html.Div(className='four columns div-user-controls',
                     children=[

                     html.H1("Real-Time Crypto Analysis APP "),

                     html.H2('Build Data Apps'),
                     html.P(' Build A Dashboard with CoinAPI and Dash .'),
                     html.P('Pick your crypto from the dropdown below.'),

                     html.Label('Crypto Asset'),
                         dcc.Dropdown(
                             id='cryptop',
                             options=[
                                 {'label': 'Bitcoin', 'value': 'BTC'},
                                 {'label': 'Ethereum', 'value': 'ETH'},
                                 {'label': 'Bitcoin Cash', 'value': 'BCH'},
                                 {'label': 'Litecoin', 'value': 'LTC'}
                             ],
                             value='BTC'
                         ),

                         html.Label('Time'),
                         dcc.Dropdown(
                             id='time_crypto',
                             options=[
                                 {'label': 'Minute', 'value': '1MIN'},
                                 {'label': 'Day', 'value': '10DAY'},
                                 {'label': 'Month', 'value': '6MTH'},
                                 {'label': 'year', 'value': '5YRS'}
                             ],
                             value='10DAY'
                         ),

                         dcc.Interval(
                             id='graph-update',
                             interval=1*1000,
                             n_intervals=0
                         ),

                     ]),


        html.Div(className='eight columns div-for-charts bg-grey',
                     children=[

                      dcc.Graph(id='graph',config={'displayModeBar': False}),

                         html.Div(
                             id="bottom_panel",
                             className="row div-bottom-panel",
                             children=[


html.Div(
                            className="display-inlineblock",
                            children=[
                                dcc.Dropdown(
                                    id="dropdown_positions",
                                    className="bottom-dropdown",
                                    options=[
                                        {"label": "Bitcoin", "value": "BTC"},
                                        {"label": "ETHEREUM","value": "ETH",},
                                    ],
                                    value="BTC",
                                    clearable=False,
                                    style={"border": "0px solid black"},
                                )
                            ],
                        ),








                            html.Div(id="orders_table", className="row table-orders"),

                            #html.Div(generate_table(df),className="row table-orders"),


                             ])













                     ])




        ])
    ])


# Define callback to update graph
@app.callback(
    Output('graph', 'figure'),
    [Input("cryptop", "value"),Input('time_crypto', 'value')]    #, Input('time_crypto', 'value')
)
def update_figure(currency,time_change):
    day='10DAY'
    # currency=value
    url = f'https://rest.coinapi.io/v1/ohlcv/{currency}/USD/latest?period_id={time_change}'
    #apikey = '6B081E29-633F-4CDD-9743-9219FBE0709B'
    apikey='60F4A03A-174B-4FC1-973D-D05364E6AEEB'
    #60F4A03A-174B-4FC1-973D-D05364E6AEEB
    headers = {'X-CoinAPI-Key': apikey}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    df = pd.DataFrame(data)

    fig = go.Figure(data=[go.Candlestick(x=df.time_period_start,
                                         open=df.price_open,
                                         high=df.price_high,
                                         low=df.price_low,
                                         close=df.price_close, )],

                    #   layout= go.Layout(
                    #     paper_bgcolor='rgba(0,0,0,0)',
                    #     plot_bgcolor='rgba(0,0,0,0)'
                    # )

                    )

    fig.update_layout( colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Cryptocurrency Prices', 'font': {'color': 'white'}, 'x': 0.5},)



    return fig




#UPDATE TABLE
# Define callback to update graph
@app.callback(
    Output('orders_table', 'children'),
    [Input("dropdown_positions", "value")]    #, Input('time_crypto', 'value')
)
def update_TABLE(currency):
    day='10DAY'
    # currency=value
    url = f'https://rest.coinapi.io/v1/ohlcv/{currency}/USD/latest?period_id={day}'
    #apikey = '6B081E29-633F-4CDD-9743-9219FBE0709B'
    apikey='60F4A03A-174B-4FC1-973D-D05364E6AEEB'
    #60F4A03A-174B-4FC1-973D-D05364E6AEEB
    headers = {'X-CoinAPI-Key': apikey}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    df = pd.DataFrame(data)
    table_df=generate_table(df)
    return table_df



if __name__ == '__main__':
    app.run_server(debug=True,port=806)