from Views.CandleStick import *

class CandleStickController:

    def __init__(self):
        pass

    def TryPlotly(self, stockName):

        # https://aroussi.com/post/python-yahoo-finance
        # period => 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        ticker = yf.Ticker(stockName+'.BK')
        ptl_df = ticker.history(period="1y")

        # https://www.geeksforgeeks.org/how-to-move-a-column-to-first-position-in-pandas-dataframe/
        ptl_df['Date'] = ptl_df.index
        # shift column 'Name' to first position
        first_column = ptl_df.pop('Date')

        # insert column using insert(position,column_name,
        # first_column) function
        ptl_df.insert(0, 'Date', first_column)
        ptl_df.index = [l for l in range(0,len(ptl_df))]

        print(ptl_df.head())

        def rma(x, n, y0):
            a = (n-1) / n
            ak = a**np.arange(len(x)-1, -1, -1)
            return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]

        # https://investexcel.net/how-to-calculate-macd-in-excel/
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

        # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
        df = ptl_df
        n = 14

        # df.rename(columns = {'AAPL.Close':'close'}, inplace = True)

        # RS
        df['change'] = df.Close.diff() # Calculate change
        df['gain'] = df.change.mask(df.change < 0, 0.0)
        df['loss'] = -df.change.mask(df.change > 0, -0.0)
        df['avg_gain'] = rma(df.gain[n+1:].to_numpy(), n, np.nansum(df.gain.to_numpy()[:n+1])/n)
        df['avg_loss'] = rma(df.loss[n+1:].to_numpy(), n, np.nansum(df.loss.to_numpy()[:n+1])/n)
        df['rs'] = df.avg_gain / df.avg_loss
        df['rsi_14'] = 100 - (100 / (1 + df.rs))


        e1 = 12
        df['ema12'] = ema(df.Close[e1:].to_numpy(), e1, np.nansum(df.Close.to_numpy()[:e1])/e1)
        e2 = 26
        df['ema26'] = ema(df.Close[e2:].to_numpy(), e2, np.nansum(df.Close.to_numpy()[:e2])/e2)
        df['macd_line'] = df.ema12 - df.ema26
        sign = 9
        df['signal'] = ema_signal(df.macd_line[e2+sign-1:].to_numpy(), sign, np.nansum(df.macd_line.to_numpy()[e2-1:e2-1+sign])/sign,e2)
        df['histogram'] = df.macd_line - df.signal

        print(df.head())

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
                        open=df['Open'],
                        high=df['High'],
                        low=df['Low'],
                        close=df['Close'],
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

        fig.update_layout(height=800, width=1024, title_text=stockName)
        fig.show()


