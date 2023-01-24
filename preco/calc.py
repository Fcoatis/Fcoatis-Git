from google.cloud import storage
import pandas as pd

pd.options.display.float_format = '{:,.5f}'.format

def calculo():
    bucket_name = "coatis"
    blob_name = "precos/calc_precos.xlsx"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    data_bytes = blob.download_as_bytes()

    df1 = pd.read_excel(data_bytes)
    df = df1[["Data", "CDI", "IMAB5+", "US0012M", "Libor_12M"]]
    df['cdi_ind'] = 1
    df['IMAB5+ +1%'] = 1
    df['Libor_12M'] = 1
    
    df['cdi_ind'] = df['cdi_ind'].astype(float)
    df['IMAB5+ +1%'] = df['IMAB5+ +1%'].astype(float)
    df['Libor_12M'] = df['Libor_12M'].astype(float)

    for i in range(1, len(df.index)):  
        df.loc[i, 'cdi_ind'] = df.loc[i-1, 'cdi_ind']  * (1 + (( 1 + df.loc[i, 'CDI'] / 100 ) ** (1/252)) - 1) #=$C2*(1+((1+$B3/100)^(1/252))-1)
        df.loc[i, 'IMAB5+ +1%'] =  (df.loc[i-1, 'IMAB5+ +1%'] * (df.loc[i, 'IMAB5+'] / df.loc[i-1, 'IMAB5+'])) * ( 1.01 ** (1/252)) #=(E2*(D3/D2))*(1,01^(1/252))
        df.loc[i, 'Libor_12M'] = (df.loc[i-1, 'Libor_12M'] * (df.loc[i, 'US0012M'] / df.loc[i-1, 'US0012M'])) * ( 1.035 ** (1/252)) #=(H2*(G3/G2))*((1,035^(1/252)))
    
    df = df.iloc[:,[0, 1, 5, 2, 6, 3, 4]]
    print(df)