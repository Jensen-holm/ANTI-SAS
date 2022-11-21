from out.out import printc
import pandas as pd
import os


def input_filter(s: str) -> None:
    if s == ":q" or s == ":quit":
        exit()
    if s == ":h" or s == ":help":
        help()


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
        input_filter(i)
        if i in analyses.keys():
            return analyses[i]
        print("\nInvalid input, try again")


def get_file_path() -> str:
    while True:
        p: str = input("Enter the file path to a csv -> ").strip()
        input_filter(p)
        if file_exists(p) and is_csv(p):
            return p
        print("File does not exist or is not a csv file, try again")


def is_csv(path: str) -> bool:
    return True if path.endswith(".csv") else False


def file_exists(path: str) -> bool:
    return True if os.path.exists(path) else False


def read_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.apply(pd.to_numeric, errors="ignore")
    return df


def filter_nums(df: pd.DataFrame) -> pd.DataFrame:
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    return df.select_dtypes(include=numerics)


def show_cols(df: pd.DataFrame) -> None:
    print("Columns:")
    for c in df.columns:
        print(c)


def choose_vars():
    x = input("Enter the independent variable -> ")
    y = input("Enter the dependent variable -> ")
    return x, y
