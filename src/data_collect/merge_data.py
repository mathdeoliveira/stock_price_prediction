import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../../config"))

import sqlite3

from config import collected_data_db


def merge_data():
    path_collect_data_db = os.path.join(
        os.path.dirname(__file__), f"../../data/raw/{collected_data_db}"
    )
    conn = sqlite3.connect(path_collect_data_db)
    cursor = conn.cursor()

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS merged_data AS
            SELECT stocks_data.Date, 
                   stocks_data.JPM,
                   stocks_data.BAC,
                   stocks_data.WFC,
                   currency_data.DEXUSUK,
                   currency_data.DEXUSEU, 
                   indices_data.SP500,
                   indices_data.DJIA,
                   indices_data.VIXCLS
            FROM stocks_data
            LEFT JOIN currency_data ON stocks_data.Date = currency_data.Date
            LEFT JOIN indices_data ON stocks_data.Date = indices_data.Date
        """
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    merge_data()
