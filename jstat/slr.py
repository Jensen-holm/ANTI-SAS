from dataclasses import dataclass, field
from jstat.model import Regression
import pandas as pd
import numpy as np
from jstat.eda import scatter, histogram, qq_plot
from jstat.stat import standardize_arr


@dataclass
class SimpleLinearRegression(Regression):
    name: str = "Simple Linear Regression"
    description: str = "Describes the relationship between two quantitative variables"
    assumptions: list[str] = field(default_factory=lambda: {
        "Normality",
        "Others"
    })

    explanatory: str = ""
    response: str = ""

    def set_explanatory(self, exp: str, dataset: pd.DataFrame) -> None:
        assert (exp in dataset.columns)
        self.explanatory = exp

    def eda(self, x, y) -> None:
        scatter(x, y, x_lab=self.explanatory, y_lab=self.response)
        qq_plot(y, lab=self.response)
        histogram(x)

    def clean(self, df):
        df.dropna(inplace=True)
        arr = np.array(
            df[[self.explanatory, self.response]]
            .values, dtype='float'
        )
        return arr[:, 0], arr[:, 1]
