#!/usr/bin/env python3

"""Менеджер привычек"""

import command
import mode
from store import Store
from getch import char_input

GLOBAL_HOTKEYS = {
    'Q': command.force_quit,
    'q': command.save_quit,
    'C': command.config,
    'm': {
        '$legend': 'Mode change',
        's': mode.summary,
        'o': mode.one_by_one,
        'a': mode.one_by_one_all,
    }
}


def have_global_action(answer):
    """Обрабатывается ли этот хоткей глобально?"""
    return answer in GLOBAL_HOTKEYS

def do_global_action(answer, store):
    """Выполнить команду"""
    fn = GLOBAL_HOTKEYS[answer]
    if isinstance(fn, dict):
        second_answer = char_input(fn['$legend']+': ')
        fn = fn[second_answer]

    fn(store)



def main():
    store = Store()
    while True:
        screen = mode.summary(store)
        answer = char_input()
        if screen.respondsto(answer):
            screen.do(answer)
        if have_global_action(answer):
            do_global_action(answer, store)

if __name__ == '__main__':
    main()
