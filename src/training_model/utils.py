import os

import joblib


def save_model(model, name_file: str):
    """Save model in .joblib
    Args:
        model: model to save in joblib
        name_file: str, name for file to be save
    """
    mdir = _model_dir()
    joblib.dump(model, f"{mdir}/{name_file}.joblib")


def load_model(name_file: str):
    """Return model from model directory
    Args:
        name_file: str, name for file to be save
    Returns:
        model loaded from directory
    """
    mdir = _model_dir()
    model = joblib.load(f"{mdir}/{name_file}.joblib")
    return model


def _model_dir() -> str:
    """Return the directory models
    Returns:
        model_dir: str, models directory
    """
    model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../models")
    return model_dir
