import os


def printc(string: str, end="\n") -> str:
    """
    printc() will take in a string and split on new lines,
    and print that output to the terminal in the center of
    the screen
    param: string -> any string that you want to be printed in the
    center of standard output
    return: the newly centered string
    """
    new: str = ""
    r, _ = os.get_terminal_size()
    spl: list[str] = string.split("\n")
    for s in spl:
        c: str = s.center(r)
        new += (c + end)
    return new
