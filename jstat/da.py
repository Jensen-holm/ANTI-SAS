from dataclasses import dataclass
from jstat.model import Model


@dataclass
class DiscriminateAnalysis(Model):
    name: str = "Discriminate Analysis"
    description: str = "Discriminate Analysis"
