from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass
class Model:
    name: str
    description: str

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"

    def __hash__(self) -> int:
        return hash((self.name, self.description))


class Regression(Model):
    def set_response(self, resp: str, df: pd.DataFrame):
        assert (resp in df.columns)
        self.response = resp
