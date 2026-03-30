import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import os

# Define the file path
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'formatted_output.csv')

# Load and sort the data
df = pd.read_csv(file_path)
df = df.sort_values(by='Date')

# Initialize Dash application
app = dash.Dash(__name__)

# Create the line chart figure
fig = px.line(
    df, 
    x='Date', 
    y='Sales', 
    title='Pink Morsel Sales',
    labels={'Date': 'Date', 'Sales': 'Sales Revenue ($)'}
)

# Build the layout
app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods: Pink Morsel Visualizer',
        style={'textAlign': 'center'}
    ),
    html.P(
        children='Visualizing the impact of the Pink Morsel price increase on January 15th, 2021.',
        style={'textAlign': 'center'}
    ),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
