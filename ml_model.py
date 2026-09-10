"""Shared employee attrition model utilities for the notebook and Streamlit app."""

from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA_PATH = Path("datasets/cleaned-data/HR-Employee-Attrition-cleaned.csv")
MODEL_PATH = Path("models/employee_attrition_pipeline.joblib")
TARGET = "AttritionBinary"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the cleaned employee dataset and validate its target column."""
    data = pd.read_csv(path)
    if TARGET not in data.columns:
        raise ValueError(f"Expected target column '{TARGET}' in {path}")
    return data


def feature_columns(data: pd.DataFrame) -> list[str]:
    """Return model inputs while excluding target, label duplicate, and row ID."""
    excluded = {TARGET, "Attrition", "EmployeeNumber"}
    return [column for column in data.columns if column not in excluded]


def build_pipeline(data: pd.DataFrame) -> Pipeline:
    """Build a preprocessing and class-balanced logistic regression pipeline."""
    features = feature_columns(data)
    numeric = data[features].select_dtypes(include=["number"]).columns.tolist()
    categorical = [column for column in features if column not in numeric]

    numeric_transformer = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_transformer = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocessor = ColumnTransformer(
        [
            ("numeric", numeric_transformer, numeric),
            ("categorical", categorical_transformer, categorical),
        ]
    )
    return Pipeline(
        [
            ("preprocessor", preprocessor),
            (
                "classifier",
                LogisticRegression(
                    class_weight="balanced",
                    max_iter=2000,
                    random_state=42,
                ),
            ),
        ]
    )


def train_model(
    data: pd.DataFrame | None = None,
) -> tuple[Pipeline, pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    """Train the model and return it with test data and evaluation metrics."""
    data = load_data() if data is None else data.copy()
    features = feature_columns(data)
    x_train, x_test, y_train, y_test = train_test_split(
        data[features],
        data[TARGET],
        test_size=0.2,
        random_state=42,
        stratify=data[TARGET],
    )
    model = build_pipeline(data)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    probabilities = model.predict_proba(x_test)[:, 1]
    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "roc_auc": roc_auc_score(y_test, probabilities),
        "classification_report": classification_report(
            y_test, predictions, output_dict=True
        ),
        "y_test": y_test,
        "predictions": predictions,
        "probabilities": probabilities,
    }
    return model, x_test, y_test.to_frame(TARGET), metrics


def save_model(model: Pipeline, path: Path = MODEL_PATH) -> None:
    """Persist a fitted pipeline for the Streamlit app."""
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


def load_or_train_model(
    model_path: Path = MODEL_PATH,
) -> tuple[Pipeline, pd.DataFrame]:
    """Load the persisted model or train it when the artifact is absent."""
    data = load_data()
    if model_path.exists():
        return joblib.load(model_path), data
    model, _, _, _ = train_model(data)
    save_model(model, model_path)
    return model, data


def risk_band(probability: float) -> str:
    """Map predicted attrition probability to an actionable HR risk band."""
    if probability >= 0.60:
        return "High"
    if probability >= 0.30:
        return "Medium"
    return "Low"
