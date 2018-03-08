#!/usr/bin/env python3

"""Менеджер привычек"""

from colorama import init as init_colorama


import lib
import mode
import screens
from store import Store

def main():
    """Функция для запуска приложения"""
    store = Store()
    screen = screens.SummaryScreen(store)
    store.windows.append(screen)
    store.render()

if __name__ == '__main__':
    init_colorama()
    main()
