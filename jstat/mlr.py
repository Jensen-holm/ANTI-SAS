from dataclasses import dataclass
from jstat.model import Model


@dataclass
class MultipleLinearRegression(Model):
    name: str = "Multiple Linear Regression"
    description: str = "Multiple Linear Regression"
