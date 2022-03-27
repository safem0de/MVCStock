from tkinter import *
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
from subprocess import Popen

import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Button(self, text="Start",
               command=self.start).pack()
        self.geometry('+10+10')
        Plotter()

    def start(self):
        self.destroy()
        Call_URL = "http://127.0.0.1:8050/"
        mycmd = r'start chrome /new-tab {}'.format(Call_URL)
        Popen(mycmd,shell = True)
        
        

class Plotter():
    def __init__(self):
        self.__run_dash()

    def __run_dash(self):
        print('plot')
        app = Dash(__name__)

        app.layout = html.Div([
            html.H4('Apple stock candlestick chart'),
            dcc.Checklist(
                id='toggle-rangeslider',
                options=[{'label': 'Include Rangeslider',
                        'value': 'slider'}],
                value=['slider']
            ),
            dcc.Graph(id="graph"),
        ])

        @app.callback(
            Output("graph", "figure"), 
            Input("toggle-rangeslider", "value"))
        def display_candlestick(value):
            df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv') # replace with your own data source
            fig = go.Figure(go.Candlestick(
                x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close']
            ))

            fig.update_layout(
                xaxis_rangeslider_visible='slider' in value
            )

            return fig

        app.run_server(debug=True)
        print('server was run')


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()