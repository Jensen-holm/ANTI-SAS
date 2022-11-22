from dataclasses import dataclass
from jstat.model import Model
import pandas as pd
from eda.eda import scatter, histogram


@dataclass
class SimpleLinearRegression(Model):
    name: str = "Simple Linear Regression"
    description: str = "Simple Linear Regression"
    explanarory: str = ""
    response: str = ""

    def set_explanatory(self, exp: str, dataset: pd.DataFrame) -> None:
        assert (exp in dataset.columns)
        self.explanarory = dataset[exp]

    def set_response(self, resp: str, dataset: pd.DataFrame) -> None:
        assert (resp in dataset.columns)
        self.response = resp

    def scatter(self) -> None:
        scatter(self.explanarory, self.response)

    def histogram(self) -> None:
        histogram(self.explanarory)
        histogram(self.response)