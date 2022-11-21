from dataclasses import dataclass, field
from out.out import printc


@dataclass
class Prompt:

    analyses: dict[str, str] = field(default_factory=lambda: {
        "1": "Discriminate Analysis",
        "2": "Exploratory Factor Analysis",
        "3": "Simple Linear Regression",
        "4": "Multiple Linear Regression"
    })

    def __str__(self) -> str:
        s: str = ""
        for i, v in self.analyses.items():
            s += printc(i, end=" ")
            s += printc(v)
        return s

    def select_analysis(self) -> str:
        print(self)
        p: str = "Select a model"
        while True:
            printc(p, end=" ")
            i = input() 
            if i in self.analyses.keys():
                return self.analyses[i]
            printc("\nInvalid input, try again")
