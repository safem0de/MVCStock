from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

import pandas as pd

import matplotlib.pyplot as plt
from mplfinance import mplfinance
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import yfinance as yf
from yahoofinancials import YahooFinancials

class CandleStickChart(ttk.Frame):

    ticker = yf.Ticker('PTG.BK')
    ptl_df = ticker.history(period="1y")

    ptl_df.head()

    def __init__(self,parent):
        super().__init__(parent)

        #create widgets
        self.labelheader = ttk.Label(self, text = 'CandleStick')
        self.labelheader.grid(row=0, column=0, sticky=tk.W)

        # self.figure = plt.Figure(figsize=(6,5), dpi=100)
        # self.ax = self.figure.add_subplot(111)
        # self.chart_type = FigureCanvasTkAgg(self.figure, self)
        # self.chart_type.get_tk_widget().grid(row=1, column=0, sticky=tk.W)
        # self.ptl_df.plot(kind='bar', legend=True, ax=self.ax)
        # self.ax.set_title('The Title for your chart')

        # mplfinance.plot(self.ptl_df, type="candle")
        self.fig, self._ = mplfinance.plot(self.ptl_df, type='candlestick', volume=True, returnfig=True, figscale=1.5)
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        # Draw it
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky=tk.W)
        
