from kfp.dsl import component

@component
def validate_model(
    model_dir: str,
    min_r2: float,
    max_mae: float,
):
    import json, os

    with open(os.path.join(model_dir, "metrics.json")) as f:
        metrics = json.load(f)

    if metrics["r2"] < min_r2:
        raise ValueError("R2 abaixo do esperado")

    if metrics["mae"] > max_mae:
        raise ValueError("MAE acima do esperado")

    print("✅ Modelo aprovado no gate")
