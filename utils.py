import yfinance as yf 
import pandas as pd 
from datetime import datetime, timedelta
import os 

# ---- Define Tickers ----- # 
tickers = ["MSFT"]

# fonctions qui télécharge les stocks 
def load_stock_data(tickers, years_back=20):
    end_date = datetime.today()
    start_date = end_date - timedelta(days=years_back * 365)
    print(f"Téléchargement des données de {start_date.date()} à {end_date.date()}")

    close_df = pd.DataFrame()

    for ticker in tickers:
        print(f"Téléchargement en cours pour {ticker}...")
        data = yf.download(ticker, start=start_date, end=end_date)
        close_df[f"{ticker}_Open"] = data['Open']
        close_df[f"{ticker}_High"] = data['High']
        close_df[f"{ticker}_Low"] = data['Low']
        close_df[f"{ticker}_Close"] = data['Close']
        close_df[f"{ticker}_Volume"] = data['Volume']
        
    
    return close_df
#fonctions qui enregistre en csv 
def save_to_csv(dataframe, filename="historical_data.csv"):
    path = "data/"
    dataframe.to_csv(path + filename)
    print(f"Données sauvegardées dans le fichier {filename}")

df = load_stock_data(tickers)
save_to_csv(df)
