import os
import sys
from typing import Tuple

import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

sys.path.append(os.path.join(os.path.dirname(__file__), "../data_process"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../training_model"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../config"))

from data_preparation import DataPreparation
from process_data import processing_data
from reframe_data import DataReframing
from utils import save_model

from config import validation_size


class TrainModel:
    """Classe para treinamento e avaliação de modelos."""

    def __init__(self):
        self.report_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../../reports/model_monitoring"
        )

    def data_processing(self) -> pd.DataFrame:
        """Carrega e processa os dados.

        Returns:
            pd.DataFrame: DataFrame contendo os dados processados.
        """
        df = processing_data()
        return df

    def data_reframer(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Executa o reenquadramento dos dados.
        Args:
            df: DataFrame processado.

        Returns:
            tuple: Tupla contendo os DataFrames X e Y processados.
        """
        dr = DataReframing(df)
        _, X, Y = dr.reframing_data()

        return X, Y

    def data_preparation(
        self,
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Prepara os dados para treinamento.

        Returns:
            tuple: Tupla contendo os DataFrames e Séries de treinamento e teste.
        """
        df = self.data_processing()
        X, Y = self.data_reframer(df)
        data_prep = DataPreparation(validation_size)
        X_train, Y_train = data_prep.create_training_data(X, Y)
        X_test, Y_test = data_prep.create_testing_data(X, Y)

        return X_train, X_test, Y_train, Y_test

    def train_model(self) -> Lasso:
        """Treina e avalia o modelo Lasso.

        Returns:
            Lasso: Modelo Lasso treinado.
        """
        X_train, X_test, Y_train, Y_test = self.data_preparation()
        model = Lasso(alpha=0.003109818155626185, max_iter=100)
        model.fit(X_train, Y_train)

        self._evaluate_model(model, X_test, Y_test)

        save_model(model, "lasso")

        return model

    def _evaluate_model(self, model, X_test: pd.DataFrame, Y_test: pd.Series):
        """Avalia o modelo calculando o erro médio quadrado e escreve o resultado em um arquivo TXT.

        Args:
            modelo: O modelo treinado.
            X_teste (pd.DataFrame): DataFrame de teste.
            Y_teste (pd.Series): Série alvo de teste.
        """
        predicted_tuned = model.predict(X_test)
        mse = mean_squared_error(Y_test, predicted_tuned)

        # Nome do arquivo de saída
        output_file = os.path.join(self.report_path, "resultado_metrica.txt")

        # Abrir o arquivo no modo de escrita, criando-o se não existir ou anexando a ele
        with open(output_file, "a") as file:
            # Escrever o resultado da métrica no arquivo
            file.write(f"Data da execução: {pd.Timestamp.now()}\n")
            file.write(f"Mean Squared Error (MSE): {mse}\n\n")


if __name__ == "__main__":
    tm = TrainModel()
    tm.train_model()
