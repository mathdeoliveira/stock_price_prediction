"""
Este código baixa os dados de ações de uma fonte de dados e os salva em um arquivo CSV.

Argumentos:
    tickers (list): Lista de tickers de ações para baixar os dados.
    start_date (str): Data inicial dos dados.
    end_date (str): Data final dos dados.

Resultado:
    Salva os dados de ações em um arquivo CSV.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../../config"))

import sqlite3
import pandas as pd
import yfinance as yf

yf.pdr_override()
from pandas_datareader import data as pdr

from config import end_date, start_date, collected_data_db, tickers


def download_stock_data():
    """
    Baixa os dados de ações de uma fonte de dados e os salva em um arquivo CSV.

    Argumentos:
        tickers (list): Lista de tickers de ações para baixar os dados.
        start_date (str): Data inicial dos dados.
        end_date (str): Data final dos dados.

    Resultado:
        Salva os dados de ações em um arquivo CSV.
    """
    # Conectar-se ao banco de dados SQLite
    
    conn = sqlite3.connect(collected_data_db)
    cursor = conn.cursor()
    
    # Criar uma tabela para armazenar os dados das moedas
    cursor.execute('''CREATE TABLE IF NOT EXISTS stocks_data (
                      Date TEXT,
                      JPM REAL,
                      BAC REAL,
                      WFC REAL)''')

    portfolio = pd.DataFrame()
    for t in tickers:
        portfolio[t] = pdr.get_data_yahoo(t, start_date, end_date)["Adj Close"]

    portfolio.reset_index().to_sql('stocks_data', conn, if_exists='replace',index=False)


if __name__ == "__main__":
    download_stock_data()
