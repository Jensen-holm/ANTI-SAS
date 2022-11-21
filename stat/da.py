from dataclasses import dataclass
from model import Model


@dataclass
class DiscriminateAnalysis(Model):
    name: str = "Discriminate Analysis"
    description: str = "Discriminate Analysis"
