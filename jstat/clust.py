from dataclasses import dataclass
from jstat.model import Model


@dataclass
class ClusterAnalysis(Model):
    name: str = "Cluster Analysis"
    description: str = "Cluster Analysis"
