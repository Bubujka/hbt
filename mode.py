"""Режимы в приложении"""

import screens

def summary(store):
    store.windows.append(screens.SummaryScreen(store))

def one_by_one(store):
    store.windows.append(screens.OneByOneScreen(store))

def one_by_one_all(store):
    store.windows.append(screens.OneByOneScreen(store))
