import os

import numpy as np
import pandas as pd


class DataReframing:
    """
    Classe para processar os dados de acordo com as etapas fornecidas.
    """

    def __init__(self, df: pd.DataFrame, return_period: int = 5):
        """
        Inicializa o processador de dados.

        Args:
            df (pd.DataFrame): O DataFrame com os dados.
            return_period (int, optional): O período de retorno para o cálculo das diferenças. Padrão é 5.
        """
        self.df = df
        self.return_period = return_period
        self.data_interim_path = os.path.join(
            os.path.dirname(__file__), "../../data/interim"
        )

    def calculate_Y(self) -> pd.Series:
        """
        Calcula a série Y, que é a diferença logarítmica deslocada de "JPM" pelo período de retorno.

        Returns:
            pd.Series: A série Y calculada.
        """
        Y = (
            np.log(self.df.loc[:, "JPM"])
            .diff(self.return_period)
            .shift(-self.return_period)
        )
        Y.name = Y.name + "_pred"
        return Y

    def calculate_X1(self) -> pd.DataFrame:
        """
        Calcula o DataFrame X1, que contém as diferenças logarítmicas de "BAC" e "WFC" pelo período de retorno.

        Returns:
            pd.DataFrame: O DataFrame X1 calculado.
        """
        X1 = np.log(self.df.loc[:, ("BAC", "WFC")]).diff(self.return_period)
        return X1

    def calculate_X2(self) -> pd.DataFrame:
        """
        Calcula o DataFrame X2, que contém as diferenças logarítmicas de "DEXUSUK" e "DEXUSEU" pelo período de retorno.

        Returns:
            pd.DataFrame: O DataFrame X2 calculado.
        """
        X2 = np.log(self.df.loc[:, ("DEXUSUK", "DEXUSEU")]).diff(self.return_period)
        return X2

    def calculate_X3(self) -> pd.DataFrame:
        """
        Calcula o DataFrame X3, que contém as diferenças logarítmicas de "SP500", "DJIA" e "VIXCLS" pelo período de retorno.

        Returns:
            pd.DataFrame: O DataFrame X3 calculado.
        """
        X3 = np.log(self.df.loc[:, ("SP500", "DJIA", "VIXCLS")]).diff(
            self.return_period
        )
        return X3

    def calculate_X4(self) -> pd.DataFrame:
        """
        Calcula o DataFrame X4, que contém as diferenças logarítmicas de "JPM" para diferentes períodos de retorno.

        Returns:
            pd.DataFrame: O DataFrame X4 calculado.
        """
        X4 = pd.concat(
            [
                np.log(self.df.loc[:, "JPM"]).diff(i)
                for i in [
                    self.return_period,
                    self.return_period * 3,
                    self.return_period * 6,
                    self.return_period * 12,
                ]
            ],
            axis=1,
        )
        X4.columns = ["JPM_DT", "JPM_3DT", "JPM_6DT", "JPM_12DT"]
        return X4

    def reframing_data(self) -> tuple:
        """
        Processa os dados e retorna as séries Y e X após a concatenação e limpeza.

        Returns:
            tuple: Uma tupla contendo a série Y e o DataFrame X processados.
        """
        Y = self.calculate_Y()
        X1 = self.calculate_X1()
        X2 = self.calculate_X2()
        X3 = self.calculate_X3()
        X4 = self.calculate_X4()

        X = pd.concat([X1, X2, X3, X4], axis=1)
        dataset = pd.concat([Y, X], axis=1).dropna().iloc[:: self.return_period, :]
        Y = dataset.loc[:, Y.name]
        X = dataset.loc[:, X.columns]

        # Salvar o DataFrame reenquadrado em um arquivo CSV no diretório 'data/interim'

        file_name = os.path.join(self.data_interim_path, "reframed_data.csv")
        dataset.to_csv(file_name)

        return dataset, X, Y
