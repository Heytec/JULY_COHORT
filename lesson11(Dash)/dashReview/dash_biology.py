import dash_bio as dashbio
import dash
#https://dash.plotly.com/dash-core-components
import dash_core_components as dcc
#https://dash.plotly.com/dash-html-components
import dash_html_components as html
import six.moves.urllib.request as urlreq
import json



# external  css from the web
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__,external_stylesheets=external_stylesheets)




data = urlreq.urlopen(
 "https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/" +
 "alignment_viewer_p53.fasta"
).read().decode("utf-8")


sequences = [{
        'sequence': 'AUGGGCCCGGGCCCAAUGGGCCCGGGCCCA',
        'structure': '.((((((())))))).((((((()))))))',
        'options': {
            'applyForce': True,
            'circularizeExternal': True,
            'avoidOthers': True,
            'labelInterval': 5,
            'name': 'PDB_01019'
        }
}]


model_data = urlreq.urlopen(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/' +
    'master/mol3d/model_data.js'
).read()
styles_data = urlreq.urlopen(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/' +
    'master/mol3d/styles_data.js'
).read()

model_data = json.loads(model_data)
styles_data = json.loads(styles_data)


app.layout=html.Div(
    children=[
    dashbio.AlignmentChart(
  id='my-dashbio-alignmentchart',
  data=data
),

dashbio.FornaContainer(
  id='my-dashbio-fornacontainer',
  sequences=sequences
),
dashbio.Molecule3dViewer(
  id='my-dashbio-molecule3dviewer',
  modelData=model_data,
  styles=styles_data,
  backgroundOpacity='0'
)


    ])




if __name__ == '__main__':
    app.run_server(debug=True)
