from dataclasses import dataclass
from jstat.model import Model


@dataclass
class SimpleLinearRegression(Model):
    name: str = "Simple Linear Regression"
    description: str = "Simple Linear Regression"
