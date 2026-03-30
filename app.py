import dash
from dash import dcc, html, Input, Output
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
app.title = "Soul Foods Visualizer"

# Build the layout
app.layout = html.Div(children=[
    html.Div(id='header-container', children=[
        html.H1(children='Soul Foods'),
        html.P(children='Pink Morsel Sales Visualizer', className='subtitle')
    ]),

    html.Div(id='main-content', children=[
        html.Div(className='radio-group-container', children=[
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': 'All Regions', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'}
                ],
                value='all',
                className='radio-group',
                inline=True
            )
        ]),
        
        html.Div(className='chart-container', children=[
            dcc.Graph(id='sales-line-chart')
        ])
    ])
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    # Filter the dataframe based on the selected region
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    # Create the line chart figure
    fig = px.line(
        filtered_df, 
        x='Date', 
        y='Sales', 
        title=f'Pink Morsel Sales - {selected_region.title()} Region',
        labels={'Date': 'Date', 'Sales': 'Sales Revenue ($)'},
        color_discrete_sequence=['#ff4b4b']
    )
    
    # Update layout for a premium dark theme aesthetic
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#ffffff',
        title_font_size=22,
        title_x=0.5, # Center the title
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor='#333333', zeroline=False),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    
    # Add hover mode customization
    fig.update_traces(mode='lines', hovertemplate='Date: %{x}<br>Sales: $%{y:.2f}<extra></extra>')
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
