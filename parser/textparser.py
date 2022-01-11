import re


def SplitSpaceColon(target):
    return re.split(r'\s{5,}|:', target)


def RemoveWhiteSpace(target: list[str]):
    while "" in target:
        target.remove("")
    return target

def ColonSplit(target:list[str]) -> list[str]:
    return re.split(" : ", target)