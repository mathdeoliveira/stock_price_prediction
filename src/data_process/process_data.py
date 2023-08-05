import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), "../../config"))

import sqlite3
import pandas as pd

from config import date_to_index, collected_data_db

def data_load() -> pd.DataFrame:
    """
    Carrega os dados da tabela merged_data do banco sqlite3 criado a partir da etapa de data_collect

    Returns:
        pd.DataFrame: O DataFrame carregado a partir do banco de dados
    """
    path_collect_data_db = os.path.join(os.path.dirname(__file__), f"../../data/raw/{collected_data_db}")
    conn = sqlite3.connect(path_collect_data_db)
    df = pd.read_sql('select * from merged_data', conn)
    conn.close()
    return df

def cleaned_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa os dados do DataFrame removendo linhas com valores ausentes (NaN) e define a data como índice.    
    Args:
        df (pd.DataFrame): O DataFrame a ser limpo. 
    Returns:
        pd.DataFrame: O DataFrame limpo com linhas sem valores ausentes e a data definida como índice.
    """
    cleaned_df = df.dropna().set_index(date_to_index)
    return cleaned_df   
    
def processing_data() -> pd.DataFrame:
    """
    Realiza todo o processamento dos dados:

    - Mescla as tabelas em um único DataFrame.
    - Limpa os dados removendo linhas com valores ausentes (NaN) e define a data como índice.
    - Salva o DataFrame limpo em um arquivo CSV no diretório 'data/interim'.

    Returns:
        pd.DataFrame: O DataFrame final, após o processamento completo dos dados.
    """

    # Mesclar os DataFrames em um único DataFrame
    df = data_load()
    
    # Limpar os dados removendo linhas com valores ausentes (NaN) e definir a data como índice
    df = cleaned_data(df)
    
    # Corrigir data do index
    df.index = pd.to_datetime(df.index).date
    # Definir o nome do índice como "Date"
    df.index.name = "Date"

    # Salvar o DataFrame limpo em um arquivo CSV no diretório 'data/interim'
    data_interim_path = os.path.join(
        os.path.dirname(__file__), "../../data/interim"
    )
    file_name = os.path.join(data_interim_path, "cleaned_data.csv")
    df.to_csv(file_name)

    return df

if __name__ == "__main__":
    processing_data()