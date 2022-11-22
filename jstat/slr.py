from dataclasses import dataclass, field
from jstat.model import Regression
import pandas as pd
import numpy as np
from jstat.eda import scatter, histogram


@dataclass
class SimpleLinearRegression(Regression):
    name: str = "Simple Linear Regression"
    description: str = "Describes the relationship between two quantitative variables"
    explanatory: str = ""
    response: str = ""

    def set_explanatory(self, exp: str, dataset: pd.DataFrame) -> None:
        assert (exp in dataset.columns)
        self.explanatory = exp

    def eda(self, df) -> None:
        scatter(df[self.explanatory], df[self.response])
        histogram(df[self.explanatory])
        histogram(df[self.response])
