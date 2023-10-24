"""
Este código baixa os dados de índices de uma fonte de dados e os salva 
em um arquivo CSV.

Argumentos:
    indices (list): Lista de índices para baixar os dados.
    fred_source (str): Fonte de dados dos índices.
    start_date (str): Data inicial dos dados.
    end_date (str): Data final dos dados.

Resultado:
    Salva os dados de índices em um arquivo CSV.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../../config"))

import sqlite3

import pandas_datareader as pdr

from config import collected_data_db, end_date, indices, start_date


def download_index_data():
    """
    Baixa os dados de índices de uma fonte de dados e os salva em um arquivo CSV.

    Argumentos:
        indices (list): Lista de índices para baixar os dados.
        fred_source (str): Fonte de dados dos índices.
        start_date (str): Data inicial dos dados.
        end_date (str): Data final dos dados.

    Resultado:
        Salva os dados de índices em um arquivo CSV.
    """
    # Conectar-se ao banco de dados SQLite

    conn = sqlite3.connect(collected_data_db)
    cursor = conn.cursor()

    # Criar uma tabela para armazenar os dados das moedas
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS indices_data (
                      Date TEXT,
                      SP500 REAL,
                      DJIA REAL,
                      VIXCLS REAL)"""
    )

    # Baixar os dados das indices
    data_indicies = pdr.get_data_fred(indices, start_date, end_date).reset_index()

    # Inserir os dados na tabela
    data_indicies.to_sql("indices_data", conn, if_exists="replace", index=False)

    # Commit e fechar a conexão com o banco de dados
    conn.commit()
    conn.close()


if __name__ == "__main__":
    download_index_data()
