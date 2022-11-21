from out.out import printc


analyses: dict[str, str] = {
    "1": "Discriminate Analysis",
    "2": "Exploratory Factor Analysis",
    "3": "Simple Linear Regression",
    "4": "Multiple Linear Regression",
    "5": "Cluster Analysis",
}


def show_options() -> None:
    print(printc("\nSelect an analysis:"))
    for k, v in analyses.items():
        print(printc(f"{k}: {v}"))


def select_analysis() -> str:
    show_options()
    p: str = "Select a model -> "
    while True:
        print(p, end=" ")
        i = input()
        if i in analyses.keys():
            return analyses[i]
        print("\nInvalid input, try again")
