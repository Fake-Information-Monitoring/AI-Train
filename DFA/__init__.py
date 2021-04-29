# -*- coding:utf-8 -*-
from DFA.DFAFilter import DFAFilter

#
# def getFilter(path: str, type: int):
#     model = DFAFilter(type)
#     model.parse(path)
#     return model


def getFilterByData(data: str, type: str):
    model = DFAFilter(type)
    model.parse_by_data(data)
    return model
