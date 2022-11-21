from dataclasses import dataclass
from jstat.model import Model


@dataclass
class ExploratoryFactorAnalysis(Model):
    name: str = "Exploratory Factor Analysis"
    description: str = "Exploratory Factor Analysis"
