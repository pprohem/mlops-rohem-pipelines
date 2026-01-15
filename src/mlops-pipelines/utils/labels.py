def build_labels(
    model_name: str,
    environment: str,
    run_id: str,
):
    return {
        "model": model_name,
        "env": environment,
        "run_id": run_id,
        "managed_by": "mlops-pipelines",
    }
