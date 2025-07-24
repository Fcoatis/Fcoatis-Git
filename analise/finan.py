import yfinance as yf
import matplotlib.pyplot as plt

msft = yf.download('MSFT', start='2016-01-01')
ibov = yf.download('^BVSP', start='2016-01-01')


# Plot the prices of MSFT and IBOV in a graph
plt.plot(msft['Adj Close'], label='MSFT')
plt.plot(ibov['Close'], label='IBOV')
plt.legend()
plt.show()
exit()