from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

# import pandas as pd
# import io
# from PIL import Image, ImageTk

# import matplotlib.pyplot as plt
# import mplfinance as mpf
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import yfinance as yf
from yahoofinancials import YahooFinancials

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd
import numpy as np

class CandleStickChart(ttk.Frame):

    # https://aroussi.com/post/python-yahoo-finance
    # period => 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    ticker = yf.Ticker('PTG.BK')
    ptl_df = ticker.history(period="6mo")

    # print(ptl_df.head())

    def __init__(self,parent):
        super().__init__(parent)

        #create widgets
        self.labelheader = ttk.Label(self, text = 'CandleStick')
        self.labelheader.grid(row=0, column=0, sticky=tk.W)

        self.TryPlotly()

        # self.image_label = ttk.Label(self)
        # self.image_reference = None
        # self.image_label.grid(row=1, column=0, sticky=tk.W)

        # self.get_image_and_display()

        # self.figure = plt.Figure(figsize=(6,5), dpi=100)
        # self.ax = self.figure.add_subplot(111)
        # self.chart_type = FigureCanvasTkAgg(self.figure, self)
        # self.chart_type.get_tk_widget().grid(row=1, column=0, sticky=tk.W)
        # self.ptl_df.plot(kind='bar', legend=True, ax=self.ax)
        # self.ax.set_title('The Title for your chart')

        # self.fig, self._ = mpf.plot(self.ptl_df, type='candle', style='charles', volume=True, returnfig=True, figscale=1.0)
        # self.canvas = FigureCanvasTkAgg(self.fig, self)
        # # Draw it
        # self.canvas.draw()
        # self.canvas.get_tk_widget().grid(row=1, column=0, sticky=tk.W)
        
    # https://github.com/matplotlib/mplfinance/issues/170
    # def get_image_and_display(self):
    #     security_dataframe = pd.DataFrame(self.ptl_df)
    #     # security_dataframe.set_index('Date', inplace=True)

    #     img_buffer = io.BytesIO()
    #     mpf.plot(security_dataframe, type='candle', style='yahoo', volume=True, show_nontrading=False, savefig=dict(fname=img_buffer, dpi=100), figscale=1.0)
    #     plt.close('all')
    #     img_buffer.seek(0)

    #     pil_image = Image.open(img_buffer)
    #     # pil_image = pil_image.resize((self.root.winfo_width(), self.root.winfo_height() - (self.root.winfo_reqheight() - self.image_label.winfo_height())))
    #     self.image_reference = ImageTk.PhotoImage(pil_image)
    #     self.image_label.configure(image=self.image_reference)
    #     self.image_label.image = self.image_reference

    def TryPlotly(self):

        def rma(x, n, y0):
            a = (n-1) / n
            ak = a**np.arange(len(x)-1, -1, -1)
            return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]

        def ema(x, n, y0):
            a = (n-1)/(n+1) # n=12 => 11/13
            k = np.arange(len(x)-1, -1, -1)
            m = np.arange(1, len(x)+1)
            ak = a**k

            return np.r_[np.full(n-1, np.nan), y0, np.cumsum(ak * x)/ak/((n+1)/2) + y0 * a**m]

        def ema_signal(x, n, y0, e2):
            a = (n-1)/(n+1) # n=12 => 11/13
            k = np.arange(len(x)-1, -1, -1)
            m = np.arange(1, len(x)+1)
            ak = a**k

            return np.r_[np.full((e2-1)+(n-1), np.nan), y0, np.cumsum(ak * x)/ak/((n+1)/2) + y0 * a**m]

        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
        n = 14

        df.rename(columns = {'AAPL.Close':'close'}, inplace = True)

        # RSI
        df['change'] = df.close.diff() # Calculate change
        df['gain'] = df.change.mask(df.change < 0, 0.0)
        df['loss'] = -df.change.mask(df.change > 0, -0.0)
        df['avg_gain'] = rma(df.gain[n+1:].to_numpy(), n, np.nansum(df.gain.to_numpy()[:n+1])/n)
        df['avg_loss'] = rma(df.loss[n+1:].to_numpy(), n, np.nansum(df.loss.to_numpy()[:n+1])/n)
        df['rs'] = df.avg_gain / df.avg_loss
        df['rsi_14'] = 100 - (100 / (1 + df.rs))


        e1 = 12
        df['ema12'] = ema(df.close[e1:].to_numpy(), e1, np.nansum(df.close.to_numpy()[:e1])/e1)
        e2 = 26
        df['ema26'] = ema(df.close[e2:].to_numpy(), e2, np.nansum(df.close.to_numpy()[:e2])/e2)
        df['macd_line'] = df.ema12 - df.ema26
        sign = 9
        df['signal'] = ema_signal(df.macd_line[e2+sign-1:].to_numpy(), sign, np.nansum(df.macd_line.to_numpy()[e2-1:e2-1+sign])/sign,e2)
        df['histogram'] = df.macd_line - df.signal

        fig = make_subplots(rows=4, cols=1, row_heights=[0.5, 0.1, 0.2, 0.2])

        reference_line_lower = go.Scatter( x=[df['Date'].iloc[0],df['Date'].iloc[-1]],
                                    y=[30, 30],
                                    name="RSI30",
                                    mode="lines",
                                    line=go.scatter.Line(color='rgba(0, 0, 0, 0.3)'),
                                    showlegend=False)

        reference_line_upper = go.Scatter( x=[df['Date'].iloc[0],df['Date'].iloc[-1]],
                                    y=[70, 70],
                                    name="RSI70",
                                    mode="lines",
                                    line=go.scatter.Line(color='rgba(0, 0, 0, 0.3)'),
                                    showlegend=False)

        fig.add_trace(
            go.Candlestick(x=df['Date'],
                        open=df['AAPL.Open'],
                        high=df['AAPL.High'],
                        low=df['AAPL.Low'],
                        close=df['close'],
                        name="CandleStick"),
                    row=1, col=1
        )

        fig.add_trace(
            go.Scatter(x=df['Date'],
                    y=df['ema12'],
                    line=dict(color='blue', width=0.8),
                    name="EMA12"),
            row=1, col=1
        )

        fig.add_trace(
            go.Scatter(x=df['Date'],
                    y=df['ema26'],
                    line=dict(color='orange', width=0.8),
                    name="EMA26"),
            row=1, col=1
        )

        fig.add_trace(
            go.Bar(x=df['Date'],
                    y=df['histogram'],
                    marker_color='crimson',
                    name='MACD_Histogram'),
            row=3, col=1
        )

        fig.add_trace(
            go.Scatter(x=df['Date'],
                    y=df['signal'],
                    marker_color='gold',
                    line=dict(width=0.5),
                    name='signal'),
            row=3, col=1
        )

        fig.add_trace(
            go.Scatter(x=df['Date'],
                    y=df['macd_line'],
                    marker_color='cyan',
                    line=dict(width=0.5),
                    name='MACD'),
            row=3, col=1
        )

        fig.add_trace(reference_line_lower, row=4, col=1)
        fig.add_trace(reference_line_upper, row=4, col=1)

        fig.add_trace(
            go.Scatter(x=df['Date'], y=df['rsi_14'],marker_color='rgba(255, 182, 193, 1)',name="RSI"),
            row=4, col=1
        )

        fig.update_layout(height=800, width=1024, title_text="AAPL")
        fig.show()
