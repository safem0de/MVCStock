from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

# import pandas as pd
# import io
# from PIL import Image, ImageTk

# import matplotlib.pyplot as plt
# import mplfinance as mpf
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# import yfinance as yf
# from yahoofinancials import YahooFinancials

# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# import pandas as pd
# import numpy as np

class CandleStickChart(ttk.Frame):

    def __init__(self,parent):
        super().__init__(parent)

        #create widgets
        self.labelheader = ttk.Label(self, text = 'CandleStick')
        self.labelheader.grid(row=0, column=0, sticky=tk.W)

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
