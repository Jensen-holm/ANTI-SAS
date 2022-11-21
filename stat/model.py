from dataclasses import dataclass


@dataclass
class Model:
    name: str
    description: str

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Model):
            return NotImplemented
        return self.name == other.name and self.description == other.description

    def __hash__(self) -> int:
        return hash((self.name, self.description))
