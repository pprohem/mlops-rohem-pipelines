from kfp import compiler
from pipelines.train_model import pipeline
import pathlib

OUTPUT = pathlib.Path("dist")
OUTPUT.mkdir(exist_ok=True)

compiler.Compiler().compile(
    pipeline_func=pipeline,
    package_path=str(OUTPUT / "train_pipeline.json"),
)
