from dataclasses import dataclass, field
from jstat.model import Regression
from jstat.eda import scatter, histogram
import pandas as pd


@dataclass
class MultipleLinearRegression(Regression):
    name: str = "Multiple Linear Regression"
    description: str = "Describes the relationship between a group of quantitative variables and one response variable"
    explanatory: list[str] = field(default_factory=lambda: [])

    def set_explanatory(self, exp, df: pd.DataFrame) -> None:
        e: list = []
        for col in exp:
            if col in df.columns:
                e.append(col)
        self.explanatory = e
        assert (len(self.explanatory > 0))
