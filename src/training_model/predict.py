import os
import sys
from typing import Tuple

import numpy as np
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), "../data_process"))

from process_data import processing_data
from reframe_data import DataReframing
from utils import load_model


class Predict:
    """Classe para predicao dos dados a partir do modelo treinado."""

    def __init__(self) -> None:
        self.model = load_model("lasso")
        self.predicted_data_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../../data/predicted"
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
        dataset, X, y = dr.reframing_data()

        return dataset, X, y

    def predict(self) -> Tuple[np.array, np.array]:
        """
        Realiza as previsões usando o modelo treinado e salve os resultados em um arquivo CSV.

        Returns:
            Tuple: Últimos dez valores reais e previstos.
        """
        df = self.data_processing()
        _, X, y = self.data_reframer(df)

        # Make predictions
        predicted_data = pd.DataFrame(self.model.predict(X), columns=["Predicted"])

        # Calculate last ten real and predicted values
        real_last_ten_dates = np.exp(y).cumprod().tail(10)
        predicted_last_ten_dates = (
            np.exp(predicted_data["Predicted"]).cumprod().tail(10)
        )

        # Save predicted data to a CSV file
        predicted_data.to_csv(os.path.join(self.predicted_data_path, "predicted.csv"))

        return real_last_ten_dates, predicted_last_ten_dates


if __name__ == "__main__":
    pred = Predict()
    pred.predict()
