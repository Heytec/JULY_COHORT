# get streamlit 
import streamlit as st 
import pandas as pd 
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from bokeh.plotting import figure

########################### Display text ###########################################
#Display text
st.text('Welcome to  africa data School.')

#Display string formatted as Markdown.
st.markdown('showing markdown **_really_ cool**.')

#Display mathematical expressions formatted as LaTeX.
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

#  (st.write) This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it

#example 1 
st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
 }))


#example 2

df = pd.DataFrame(
    np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)



#Display text in title formatting.
st.title('This is a title')

#Display text in header formatting.
st.header('This is a header')

#Display text in subheader formatting.
st.subheader('This is a subheader')

#Display a code block with optional syntax highlighting.
code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')



#############################################Display data###################################

#Display a dataframe as an interactive table.
df = pd.DataFrame(  np.random.randn(50, 20),columns=('col %d' % i for i in range(20)))
st.dataframe(df)

#Display a static table.
df = pd.DataFrame(   np.random.randn(10, 5),columns=('col %d' % i for i in range(5)))
st.table(df)

#Display object or string as a pretty-printed JSON string.
st.json({
     'foo': 'bar',
    'baz': 'boz',
     'stuff': [
         'stuff 1',
        'stuff 2',
       'stuff 3',
        'stuff 5',
    ], })


###########################Display charts#########################################

#Display a line chart.

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
   columns=['a', 'b', 'c'])
st.line_chart(chart_data)


#Display a area chart.
chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
st.area_chart(chart_data)


#Display a bar chart.
chart_data = pd.DataFrame(    np.random.randn(50, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)


#Display a matplotlib.pyplot figure.
arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)
st.pyplot()

#Display a chart using the Altair library.
df = pd.DataFrame(np.random.randn(200, 3),columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.altair_chart(c, use_container_width=True)

#Display a chart using the Vega-Lite library.
df = pd.DataFrame(     np.random.randn(200, 3),columns=['a', 'b', 'c'])
st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
         'color': {'field': 'c', 'type': 'quantitative'},     }, })


#Display an interactive Plotly chart.

 # Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

 # Group data together
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
# Plot!
st.plotly_chart(fig, use_container_width=True)


#Display an interactive Bokeh chart.
from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure( x_axis_label='x', y_axis_label='y')
p.line(x, y, legend='Trend', line_width=2)
st.bokeh_chart(p, use_container_width=True)


#Display a map with points on it.
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon']) 
st.map(df)



##############################################################Display media##############################

#Display an image or list of images.
from PIL import Image
image = Image.open('ads.png')
st.image(image, caption='Sunrise by the mountains',  use_column_width=True)


#Display an audio player.
audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')


#Display a video player.
video_file = open('pix.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)



############################################# Display interactive widgets ##################################

#Display a button widget.

if st.button('Say hello'):
     st.write('Why hello there')
else: 
     st.write('Goodbye')


# Display a checkbox widget.
agree = st.checkbox('I agree')
if agree:
        st.write('Great!')


#Display a radio button widget.

genre = st.radio(
    "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")



#Display a select widget.
option = st.selectbox(
   'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)


#Display a multiselect widget. 
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)


#Display a slider widget.
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


#Display a single-line text input widget.
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


#Display a numeric input widget.
number = st.number_input('Insert a number')
st.write('The current number is ', number)


#Display a multi-line text input widget.

txt = st.text_area('Text to analyze', '''
   It was the best of times, it was the worst of times, it was
   the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
   was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)     ''')
st.write('Sentiment:', txt)


#Display a date input widget.
import datetime
d = st.date_input(
     "When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)


#Display a file uploader widget.
#limited to 200mb

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
     data = pd.read_csv(uploaded_file)
     st.write(data)


#Display a color picker widget.
color = st.beta_color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)




#######################################Add widgets to sidebar###########################################
#Here’s an example of how you’d add a selectbox to your sidebar.
add_selectbox1 = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email1", "Home phone2", "Mobile phone2")
)



##################################Display progress and status############################
#Display a progress bar.
import time
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

#Temporarily displays a message while executing a block of code..
with st.spinner('Wait for it...'):
   time.sleep(5)
   st.success('Done!')


#Display error message.
st.error('This is an error')


#Display warning message.
st.warning('This is a warning')

#Display an informational message.
st.info('This is a purely informational message')

#Display a success message.
st.success('This is a success message!')


#@st.cache

st.balloons()