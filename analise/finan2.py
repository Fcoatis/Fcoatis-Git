import yfinance as yf
import pandas as pd
import numpy as np

ativos = ['MSFT','AAPL']
inicio = '2020-01-01'
fim = '2022-12-31'
precos = yf.download(ativos, start = inicio, end = fim)['Adj Close']
compras = {'AAPL': 1500, 'MSFT': 1400}
compras_df = pd.Series(data = compras, index = list(compras.keys()))
primeiro = precos.iloc[0]
qtd_acoes = compras_df/primeiro
PL = precos*qtd_acoes
PL['PL Total'] = PL.sum(axis = 1)
PL.index = PL.index.strftime('%m/%d/%Y')

ibov = yf.download('^BVSP', start = inicio, end =  fim)
ibov.drop(ibov.columns[[0,1,2,3,5]], axis = 1, inplace = True)
ibov.index = ibov.index.strftime('%m/%d/%Y')
consolidado = pd.merge(ibov, PL, how='inner', on='Date')
exit()