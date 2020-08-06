# import
import dash
import pandas as pd
import plotly.express as px
#https://dash.plotly.com/dash-core-components
import dash_core_components as dcc
#https://dash.plotly.com/dash-html-components
import dash_html_components as html
from dash.dependencies import Input, Output


# external  css from the web
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__,external_stylesheets=external_stylesheets)


#  dumy datasets created using pandas dataframe

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# gdp  data
df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

#gapminderDataFiveYear
df3= pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

#demostrate table data
#df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


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


################################################# create charts using plotly ######################################

# create bar chart using plotly
fig_bar = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
#fig.show()

# create sactter plot using plotly
fig_scatter = px.scatter(df2, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)


# mark down tex
markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''




#############################################app layout ##########################################################
app.layout=html.Div(
    children=[

   # title
    html.H1(children='Hello Dash',style={'width':'100%', 'margin':25, 'textAlign': 'center'}),

   #sub title
    html.Div(children='''
        Dash: A web application framework for Python.
    ''',style={'width':'100%', 'margin':25, 'textAlign': 'center'}),

   #one graph
    dcc.Graph(
        id='example-graph',
        figure=fig_bar
    ),

    #  # table with title
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df),

    # scatter plot
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig_scatter
    ),
    # table with title
    html.H4(children='life-exp-vs-gdp'),
    generate_table(df2),

    #markdown
    dcc.Markdown(children=markdown_text),

    # dropdown single select
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
    # drop down multi select
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),
    # radio
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
   # checklist
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),
    # input  text
    html.Label('Text Input'),
    dcc.Input(value='MTL', type='text'),

    # slider
    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5,
    ),

    # Graph  conntected to slide demostrate how callback  work
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df3['year'].min(),
        max=df3['year'].max(),
        value=df3['year'].min(),
        marks={str(year): str(year) for year in df3['year'].unique()},
        step=None
    )
])



@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df3[df3.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    #fig.update_layout(transition_duration=500)

    return fig











if __name__ == '__main__':
    app.run_server(debug=True)

