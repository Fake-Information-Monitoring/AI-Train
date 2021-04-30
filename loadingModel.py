import joblib


def save(model, model_name: str):
    joblib.dump(model, model_name)


def load(model_name: str):
    return joblib.load(model_name)

