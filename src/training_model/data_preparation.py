import os
import sys

import pandas as pd


class DataPreparation:
    """Classe para preparação de dados de treinamento e teste."""

    def __init__(self, validation_size: float) -> None:
        """
        Inicializa a classe DataPreparation.

        Args:
            validation_size (float): A proporção do tamanho de validação em relação ao tamanho total.
        """
        self.validation_size = validation_size

    def create_train_size(self, df: pd.DataFrame) -> int:
        """
        Calcula o tamanho dos dados de treinamento com base no tamanho de validação fornecido.

        Args:
            df (pd.DataFrame): O DataFrame de dados.

        Returns:
            int: O tamanho dos dados de treinamento.
        """
        train_size = int(len(df) * (1 - self.validation_size))
        return train_size

    def create_training_data(self, X: pd.DataFrame, Y: pd.Series) -> tuple:
        """
        Cria conjuntos de dados de treinamento com base nos DataFrames X e Y fornecidos.

        Args:
            X (pd.DataFrame): O DataFrame de recursos.
            Y (pd.Series): A Série alvo.

        Returns:
            tuple: Um par de DataFrames contendo os dados de treinamento (X_train, Y_train).
        """
        train_size = self.create_train_size(X)
        X_train, Y_train = X.iloc[:train_size], Y.iloc[:train_size]
        return X_train, Y_train

    def create_testing_data(self, X: pd.DataFrame, Y: pd.DataFrame) -> tuple:
        """
        Cria conjuntos de dados de teste com base nos DataFrames X e Y fornecidos.

        Args:
            X (pd.DataFrame): O DataFrame de recursos.
            Y (pd.DataFrame): O DataFrame alvo.

        Returns:
            tuple: Um par de DataFrames contendo os dados de teste (X_test, Y_test).
        """
        train_size = self.create_train_size(X)
        X_test, Y_test = X.iloc[train_size:], Y.iloc[train_size:]
        return X_test, Y_test
