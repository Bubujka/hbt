#!/usr/bin/env python3

"""Менеджер привычек"""

import lib
import mode
from store import Store

def main():
    """Функция для запуска приложения"""
    store = Store()
    screen = mode.summary(store)
    lib.repl_loop(store, screen)

if __name__ == '__main__':
    main()
