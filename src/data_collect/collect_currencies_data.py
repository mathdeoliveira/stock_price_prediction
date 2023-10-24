"""
Este código baixa os dados de moedas de uma fonte de dados e os salva em um arquivo CSV.

Argumentos:
    currencies (list): Lista de moedas para baixar os dados.
    fred_source (str): Fonte de dados dos dados de moedas.
    start_date (str): Data inicial dos dados.
    end_date (str): Data final dos dados.

Resultado:
    Salva os dados de moedas em um arquivo CSV.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../../config"))

import sqlite3
import pandas_datareader as pdr

from config import currencies, collected_data_db, end_date, start_date


def create_currency_database():
    # Conectar-se ao banco de dados SQLite
    
    conn = sqlite3.connect(collected_data_db)
    cursor = conn.cursor()

    # Criar uma tabela para armazenar os dados das moedas
    cursor.execute('''CREATE TABLE IF NOT EXISTS currency_data (
                      Date TEXT,
                      DEXUSUK REAL,
                      DEXUSEU REAL)''')
    

    # Baixar os dados das moedas
    data_currencies = pdr.get_data_fred(currencies, start_date, end_date).reset_index()

    # Inserir os dados na tabela
    data_currencies.to_sql('currency_data', conn, if_exists='replace',index=False)

    # Commit e fechar a conexão com o banco de dados
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    create_currency_database()