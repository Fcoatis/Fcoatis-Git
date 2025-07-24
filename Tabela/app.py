import pandas as pd
import yfinance as yf
from tqdm import tqdm
import time

# Lê o arquivo de tickers (segunda coluna)
tickers_df = pd.read_csv('Tabela/tickers_ibra.csv')
tickers = tickers_df.iloc[:, 1].astype(str).tolist()

resultados = []

# Use apenas os 10 primeiros para teste rápido
for i, tk in enumerate(tqdm(tickers[:10], desc="Buscando nomes das empresas")):
    print(f"{i+1}/{len(tickers[:10])} - Buscando: {tk}")
    try:
        yf_ticker = yf.Ticker(tk + '.SA')
        info = yf_ticker.info
        nome = info.get('longName') or info.get('shortName') or "Nome não encontrado"
    except Exception:
        nome = "Nome não encontrado"
    resultados.append({'Ticker': tk, 'Nome da Empresa': nome})
    time.sleep(0.5)  # Intervalo para evitar bloqueio do Yahoo

# Salva em CSV e imprime o resultado
df_resultado = pd.DataFrame(resultados)
df_resultado.to_csv('tickers_com_nomes.csv', index=False, encoding='utf-8-sig')
print(df_resultado)
