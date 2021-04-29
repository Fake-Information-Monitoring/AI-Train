# -*- coding:utf-8 -*-
from DFA.DFAFilter import DFAFilter


def getFilter(path: str, type: int):
    model = DFAFilter(type)
    model.parse(path)
    return model
