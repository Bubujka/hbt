"""Режимы в приложении"""

import screens

def summary(store):
    return screens.SummaryScreen(store)

def one_by_one(store):
    return screens.OneByOneScreen(store)

def one_by_one_all(store):
    return screens.OneByOneScreen(store)
