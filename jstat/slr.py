from dataclasses import dataclass, field
from jstat.model import Regression
import pandas as pd
import numpy as np
from jstat.eda import scatter, histogram


@dataclass
class SimpleLinearRegression(Regression):
    name: str = "Simple Linear Regression"
    description: str = "Describes the relationship between two quantitative variables"
    explanatory: np.array = field(default_factory=lambda: np.array([]))
    response: np.array = field(default_factory=lambda: np.array([]))

    def set_explanatory(self, exp: str, dataset: pd.DataFrame) -> None:
        assert (exp in dataset.columns)
        self.explanarory = np.array(dataset[exp])


    def eda(self) -> None:
        scatter(self.explanatory, self.response)
        histogram(self.explanarory)
        histogram(self.response)


