# import yfinance as yf
# from datetime import datetime, timedelta

# start_date = datetime.today().date() - timedelta(90)
# end_date = str(datetime.today().date())

# # Define the ticker symbols
# ticker_symbols = ['AAPL', 'MSFT', 'GOOGL']

# # Download data for multiple tickers
# data = yf.download(ticker_symbols, start=start_date, end=end_date)

# import dash
# from dash import dcc, html, dash_table, Dash
# from dash.dependencies import Input, Output
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# import pandas as pd


# # Initialize the Dash app
# # app = dash.Dash(__name__)

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = Dash(external_stylesheets=external_stylesheets)


# data.index = data.index.strftime('%Y-%m-%d')
# data_copy = data.reset_index().copy().round(2)

# data_copy.columns = [' - '.join(col).strip() for col in data_copy.columns.values]

# data_copy = data_copy.rename(columns = {'Date -':'Date'})
# # Layout of the app
# # app.layout = html.Div([
# #     html.Div(className='row', children='Stock Market Chart Comparison',
# #              style={'textAlign': 'center', 'color': 'blue', 'fontSize': 25},
# #              ),
    
             
# #     html.Div([
# #             html.Img(
# #                 src='/assets/logo.png',  # Path to your logo image in the assets folder
# #                 style={
# #                     'width': '150px',      # Adjust width as needed
# #                     'height': 'auto',      # Maintain aspect ratio
# #                     'margin': '10px'       # Optional: Add some margin around the image
# #                 }
# #             )
# #         ], style={'textAlign': 'center'})
# #     ], style={'marginBottom': '20px'}),
# #     html.Div(children=[
# #         html.Div(className='six columns', children=[
# #             dash_table.DataTable(data=data_copy.to_dict('records'), page_size = 6,
# #                                  style_data={
# #             'backgroundColor': 'lightgray',
# #             'color': 'black',
# #             'border': '1px solid blue'
# #         }, 
# #         style_cell={
# #             'textAlign': 'center',
# #             'padding': '10px'
# #         },
# #         style_header={
# #             'backgroundColor': 'darkblue',
# #             'color': 'white',
# #             'fontWeight': 'bold'
# #         })
# #         ,
        
# #             dcc.Dropdown(
# #                 id='category-dropdown',
# #                 options=[{'label': col, 'value': col} for col in ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']],
# #                 value='Adj Close',  # Default value
# #                 style={
# #                 'width': '48%',
# #                 'display': 'inline-block',
# #                 'color': 'white',                # Text color
# #                 # 'backgroundColor': 'blue',       # Background color of the dropdown box
# #                 # 'border': '1px solid black',     # Border styling
# #                 # 'borderRadius': '5px',           # Rounded corners
# #                 # 'padding': '10px',               # Padding inside the dropdown
# #                 'fontWeight': 'bold',            # Font weight
# #                 'fontSize': '16px',              # Font size
# #         }
# #             ),
# #             dcc.Dropdown(
# #                 id='subcategory-dropdown',
# #                 options=[{'label': company, 'value': company} for company in ['AAPL', 'GOOGL', 'MSFT']],
# #                 value='AAPL',  # Default value
# #                 style={
# #                 'width': '48%',
# #                 'display': 'inline-block',
# #                 'color': 'white',                # Text color
# #                 # 'backgroundColor': 'blue',       # Background color of the dropdown box
# #                 # 'border': '1px solid black',     # Border styling
# #                 # 'borderRadius': '5px',           # Rounded corners
# #                 # 'padding': '10px',               # Padding inside the dropdown
# #                 'fontWeight': 'bold',            # Font weight
# #                 'fontSize': '16px',              # Font size
# #         }
# #             ),
# #             dcc.Graph(figure = {}, id='graph')
# #         ])
# #     ])
# # ])
# # app.layout = html.Div([
# #     # Title and Logo
# #     html.Div([
# #         html.Div(
# #             'Stock Market Chart Comparison',
# #             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 25}
# #         ),
# #         html.Div([
# #             html.Img(
# #                 src=r'/assets/Stock_logo.jpg',  # Path to your logo image in the assets folder
# #                 style={
# #                     'width': '150px',      # Adjust width as needed
# #                     'height': 'auto',      # Maintain aspect ratio
# #                     'margin': '10px'       # Optional: Add some margin around the image
# #                 }
# #             )
# #         ], style={'textAlign': 'Right'})
# #     ], style={'marginBottom': '20px'}),  # Add some margin below the title and logo

# #     # Main Content
# #     html.Div([
# #         html.Div(className='six columns', children=[
# #             dash_table.DataTable(
# #                 data=data_copy.to_dict('records'),
# #                 page_size=6,
# #                 style_data={
# #                     'backgroundColor': 'lightgray',
# #                     'color': 'black',
# #                     'border': '1px solid blue'
# #                 },
# #                 style_cell={
# #                     'textAlign': 'center',
# #                     'padding': '10px'
# #                 },
# #                 style_header={
# #                     'backgroundColor': 'darkblue',
# #                     'color': 'white',
# #                     'fontWeight': 'bold'
# #                 }
# #             ),
# #             dcc.Dropdown(
# #                 id='category-dropdown',
# #                 options=[{'label': col, 'value': col} for col in ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']],
# #                 value='Adj Close',  # Default value
# #                 style={
# #                     'width': '48%',
# #                     'display': 'inline-block',
# #                     'color': 'black',                # Text color
# #                     # 'backgroundColor': 'blue',       # Background color of the dropdown box
# #                     # 'border': '1px solid black',     # Border styling
# #                     # 'borderRadius': '5px',           # Rounded corners
# #                     # 'padding': '10px',               # Padding inside the dropdown
# #                     'fontWeight': 'bold',            # Font weight
# #                     'fontSize': '16px',              # Font size
# #                 }
# #             ),
# #             dcc.Dropdown(
# #                 id='subcategory-dropdown',
# #                 options=[{'label': company, 'value': company} for company in ['AAPL', 'GOOGL', 'MSFT']],
# #                 value='AAPL',  # Default value
# #                 style={
# #                     'width': '48%',
# #                     'display': 'inline-block',
# #                     'color': 'black',                # Text color
# #                     # 'backgroundColor': 'blue',       # Background color of the dropdown box
# #                     # 'border': '1px solid black',     # Border styling
# #                     # 'borderRadius': '5px',           # Rounded corners
# #                     # 'padding': '10px',               # Padding inside the dropdown
# #                     'fontWeight': 'bold',            # Font weight
# #                     'fontSize': '16px',              # Font size
# #                 }
# #             ),
# #             dcc.Graph(figure={}, id='graph')
# #         ])
# #     ])
# # ])

# app.layout = html.Div(
#     children=[
#         # Title and Logo
#         html.Div([
#             html.Div(
#                 'Stock Market Chart Comparison',
#                 style={'textAlign': 'center', 'color': 'blue', 'fontSize': 25}
#             ),
#             html.Div([
#                 html.Img(
#                     src='/assets/Stock_logo.jpg',  # Path to your logo image in the assets folder
#                     style={
#                         'width': '150px',      # Adjust width as needed
#                         'height': 'auto',      # Maintain aspect ratio
#                         'margin': '10px'       # Optional: Add some margin around the image
#                     }
#                 )
#             ], style={'textAlign': 'Right'})
#         ], style={'marginBottom': '20px'}),  # Add some margin below the title and logo

#         # Main Content
#         html.Div([
#             html.Div(children=[
#                 dash_table.DataTable(
#                     data=data_copy.to_dict('records'),
#                     page_size=6,
#                     style_data={
#                         'backgroundColor': 'lightgray',
#                         'color': 'black',
#                         'border': '1px solid blue'
#                     },
#                     style_cell={
#                         'textAlign': 'center',
#                         'padding': '10px'
#                     },
#                     style_header={
#                         'backgroundColor': 'darkblue',
#                         'color': 'white',
#                         'fontWeight': 'bold'
#                     }
#                 ),
#                 dcc.Dropdown(
#                     id='category-dropdown',
#                     options=[{'label': col, 'value': col} for col in ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']],
#                     value='Adj Close',  # Default value
#                     style={
#                         'width': '48%',
#                         'display': 'inline-block',
#                         'color': 'black',                # Text color
#                         'fontWeight': 'bold',            # Font weight
#                         'fontSize': '16px',              # Font size
#                     }
#                 ),
#                 dcc.Dropdown(
#                     id='subcategory-dropdown',
#                     options=[{'label': company, 'value': company} for company in ['AAPL', 'GOOGL', 'MSFT']],
#                     value='AAPL',  # Default value
#                     style={
#                         'width': '48%',
#                         'display': 'inline-block',
#                         'color': 'black',                # Text color
#                         'fontWeight': 'bold',            # Font weight
#                         'fontSize': '16px',              # Font size
#                     }
#                 ),
#                 dcc.Graph(figure={}, id='graph')
#             ])
#         ])
#     ]
# )

# # Callback to update the graph based on dropdown selections
# @app.callback(
#     Output('graph', 'figure'),
#     [Input('category-dropdown', 'value'),
#      Input('subcategory-dropdown', 'value')]
# )
# def update_graph(selected_category, selected_subcategory):
#     fig = make_subplots(rows = 2, cols = 1, subplot_titles= ('Trend Chart', 'Distribution Chart'))
#     filtered_df = (data[(selected_category,selected_subcategory)])
#     fig.add_trace(go.Scatter(x = filtered_df.index, y = filtered_df.values, showlegend=False), row = 1, col=1)
#     fig.add_trace(go.Histogram(x = filtered_df.values, showlegend = False, histnorm='probability'), row = 2, col=1)
#     fig.update_layout(height = 500, width = 1800)
#     fig.update_yaxes(title_text = 'Stock Trend', row = 1, col =1)
#     fig.update_xaxes(title_text = 'Dates', row = 1, col = 1 )
#     fig.update_yaxes(title_text = 'Probability', row = 2, col=1)
#     fig.update_xaxes(title_text = 'Stock Values', row = 2, col=1)
#     fig.write_html('Test.html')
#     return fig

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)


import yfinance as yf
from datetime import datetime, timedelta
from dash import dcc, html, dash_table, Dash
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data fetching and preparation
start_date = datetime.today().date() - timedelta(90)
end_date = str(datetime.today().date())
ticker_symbols = ['AAPL', 'MSFT', 'GOOGL']
data = yf.download(ticker_symbols, start=start_date, end=end_date)
data.index = data.index.strftime('%Y-%m-%d')
data_copy = data.reset_index().copy().round(2)
data_copy.columns = [' - '.join(col).strip() for col in data_copy.columns.values]
data_copy = data_copy.rename(columns={'Date -': 'Date'})

# Initialize the Dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)
server = app.server

# Layout with improved background image and content positioning
app.layout = html.Div(
    style={
        'backgroundImage': 'url(/assets/NYSE.jpg)',  # Ensure this image is placed in the assets folder
        'backgroundSize': 'cover',       # Makes sure the image covers the entire div
        'backgroundPosition': 'center',
        'backgroundRepeat': 'no-repeat', # Prevents the image from repeating
        'height': '100vh',               # Full viewport height
        'width': '100vw',                # Full viewport width
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'flex-start',  # Align items to the top
        'alignItems': 'center',          # Center items horizontally
        'overflow': 'auto'               # Allows scrolling if content overflows
    },
    children=[
        # Title and Logo Container
        html.Div(
            style={
                    'textAlign': 'center',
                    'color': 'blue',
                    'fontSize': 25,
                    'backgroundColor': 'rgba(255, 255, 255, 0.8)',  # Box background color with transparency
                    'border': '2px solid blue',  # Border of the box
                    'padding': '10px',  # Padding inside the box
                    'borderRadius': '10px',  # Rounded corners
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'margin': '0 auto',  # Center the box horizontally
                    'width': 'fit-content',  # Box should only be as wide as its content
                },
            children=[
                # Title Box
                html.Div(
                    'Stock Market Chart Comparison',
                    style={
                        'color': 'blue',
                        'fontSize': '32px',
                        'padding': '10px 20px',
                        'backgroundColor': 'rgba(255, 255, 255, 0.8)',  # Semi-transparent background
                        'border': '2px solid blue',
                        'borderRadius': '10px',
                        'boxShadow': '2px 2px 10px rgba(0, 0, 0, 0.1)',
                        'fontWeight': 'bold'
                    }
                ),
                # Logo
                html.Img(
                    src='/assets/Stock_logo.jpg',  # Ensure this image is placed in the assets folder
                    style={
                        'width': '150px',
                        'height': 'auto',
                        'borderRadius': '10px',
                        'boxShadow': '2px 2px 10px rgba(0, 0, 0, 0.1)'
                    }
                )
            ]
        ),
        # Main Content
        html.Div(
            style={
                'width': '90%',
                'backgroundColor': 'rgba(255, 255, 255, 0.8)',  # Semi-transparent background for readability
                'padding': '20px',
                'marginTop': '20px',
                'borderRadius': '10px',
                'boxShadow': '2px 2px 10px rgba(0, 0, 0, 0.1)'
            },
            children=[
                dash_table.DataTable(
                    data=data_copy.to_dict('records'),
                    page_size=6,
                    style_data={
                        'backgroundColor': 'lightgray',
                        'color': 'black',
                        'border': '1px solid blue'
                    },
                    style_cell={
                        'textAlign': 'center',
                        'padding': '10px'
                    },
                    style_header={
                        'backgroundColor': 'darkblue',
                        'color': 'white',
                        'fontWeight': 'bold'
                    }
                ),
                html.Div(
                    style={'display': 'flex', 'justifyContent': 'space-between', 'marginTop': '20px'},
                    children=[
                        dcc.Dropdown(
                            id='category-dropdown',
                            options=[{'label': col, 'value': col} for col in ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']],
                            value='Adj Close',  # Default value
                            style={
                                'width': '48%',
                                'color': 'black',
                                'fontWeight': 'bold',
                                'fontSize': '16px',
                            }
                        ),
                        dcc.Dropdown(
                            id='subcategory-dropdown',
                            options=[{'label': company, 'value': company} for company in ['AAPL', 'GOOGL', 'MSFT']],
                            value='AAPL',  # Default value
                            style={
                                'width': '48%',
                                'color': 'black',
                                'fontWeight': 'bold',
                                'fontSize': '16px',
                            }
                        )
                    ]
                ),
                dcc.Graph(figure={}, id='graph', style={'marginTop': '20px'})
            ]
        )
    ]
)

# Callback to update the graph based on dropdown selections
@app.callback(
    Output('graph', 'figure'),
    [Input('category-dropdown', 'value'),
     Input('subcategory-dropdown', 'value')]
)
def update_graph(selected_category, selected_subcategory):
    fig = make_subplots(rows=2, cols=1, subplot_titles=('Trend Chart', 'Distribution Chart'))
    filtered_df = data[(selected_category, selected_subcategory)]
    
    # Adding the traces for the two plots
    fig.add_trace(go.Scatter(
        x=filtered_df.index, 
        y=filtered_df.values, 
        showlegend=False,
        line=dict(color='blue')
    ), row=1, col=1)
    
    fig.add_trace(go.Histogram(
        x=filtered_df.values, 
        showlegend=False, 
        histnorm='probability',
        marker=dict(color='blue')
    ), row=2, col=1)
    
    # Update layout to make background transparent
    fig.update_layout(
        height=600,
        paper_bgcolor='rgba(0.8, 0.8, 0.8, 0.8)',  # Transparent background outside the plot
        plot_bgcolor='rgba(0.8, 0.8, 0.8, 0.8)',   # Transparent background within the plot
        margin=dict(t=50, b=50, l=25, r=25)
    )
    
    # Update axis titles
    fig.update_yaxes(title_text='Stock Trend', row=1, col=1)
    fig.update_xaxes(title_text='Dates', title_font=dict(color='Black'), row=1, col=1)
    fig.update_yaxes(title_text='Probability', row=2, col=1)
    fig.update_xaxes(title_text='Stock Values', title_font=dict(color='Black'), row=2, col=1)
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

