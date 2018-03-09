"""Определение экранов в приложении"""

from colorama import Fore, Style, ansi
from functools import lru_cache

import lib
import mode

OK_CODE = '✓'
FAIL_CODE = '✗'
BLANK_CODE = '·'

class Screen():
    """Класс экрана"""
    def __init__(self, store):
        self.store = store

    def print(self):
        """Напечатать экран на экран"""
        print('Changed mode to', type(self))

    def respondsto(self, answer):
        """Понимает ли данный экран хоткей?"""
        return answer in self.hotkeys()

    def doaction(self, answer):
        """Выполнить действие для хоткея"""
        self.hotkeys()[answer]()

    def hotkeys(self):
        """Получить список хоткеев для данного экрана"""
        return {}



class OneByOneScreen(Screen):
    def __init__(self, store):
        super(OneByOneScreen, self).__init__(store)
        items = self.store.habits()
        self.habits = [h for h in items if not h.is_ok()]
        self.index = 0

    def print(self):
        if self.index == len(self.habits):
            self.store.back()

        self.store.add_window(HabitScreen(self.store, self.habits[self.index]))
        self.index += 1
        self.store.rerender()

def nice_print(habit):
    """Напечатать строку и её номер"""
    print(color_tag(habit.tag).ljust(7, " "),
          habit.name.ljust(max_name_length() + 5, " "),
          color_stats(habit.stats()),
          habit.interval_for_print())


class HabitScreen(Screen):
    def __init__(self, store, habit):
        super(HabitScreen, self).__init__(store)
        self.habit = habit

    def print(self):
        nice_print(self.habit)

    def hotkeys(self):
        return {
            'l': self.later,
            's': self.skip,
            'd': self.done,
            'u': self.undone
        }

    def later(self):
        self.store.back()

    def skip(self):
        self.habit.skip()
        self.store.save()
        self.store.back()

    def done(self):
        self.habit.done()
        self.store.save()
        self.store.back()

    def undone(self):
        self.habit.undone()
        self.store.save()
        self.store.back()

def print_with_number(habit, number):
    """Напечатать строку и её номер"""
    print(color_tag(habit.tag).ljust(7, " "),
          nice_number(number),
          habit.name.ljust(max_name_length() + 5, " "),
          color_stats(habit.stats()),
          habit.interval_for_print())


def color_stats(stats):
    """Вывести статистику в виде цветной строки"""
    return "".join([to_code(t) for t in stats])


def to_code(state):
    """Превратить буль в код"""
    if state is None:
        ret = BLANK_CODE
    elif state:
        if state.get('skip'):
            ret = 's'
        elif state.get('code') == 'auto':
            ret = OK_CODE
        else:
            ret = Fore.GREEN + OK_CODE
    else:
        ret = Fore.RED + FAIL_CODE
    return ret + Style.RESET_ALL



@lru_cache()
def max_name_length():
    """Вернуть максимальную длину названий"""
    return max([len(i['name']) for i in lib.cfg()['items']])

def nice_number(current):
    """Цифра с отступом"""
    return str(current).ljust(4)


def color_tag(tag):
    """Раскрасить тэг"""
    prefix = ""
    if tag == 'home':
        prefix = Style.BRIGHT+Fore.GREEN
    if tag == 'comp':
        prefix = Style.BRIGHT+Fore.BLUE
    if tag == 'food':
        prefix = Style.BRIGHT+Fore.MAGENTA
    return prefix+tag+Style.RESET_ALL




class SummaryScreen(Screen):
    def __init__(self, *args):
        super(SummaryScreen, self).__init__(*args)
        self.mode = 'undone'

    def print(self):
        items = self.store.habits()
        ok_items = [h for h in items if h.is_ok()]
        fail_items = [h for h in items if not h.is_ok()]

        mappings = {}

        i = 0
        if self.mode in ('all', 'undone'):
            if fail_items:
                print(Fore.RED+"Надо сделать:"+Style.RESET_ALL)
                for habit in fail_items:
                    i += 1
                    mappings[i] = habit
                    print_with_number(habit, i)
        if self.mode in ('all', 'done'):
            if ok_items:
                print(Fore.GREEN+"Сделано:"+Style.RESET_ALL)
                for habit in ok_items:
                    i += 1
                    mappings[i] = habit
                    print_with_number(habit, i)

    def hotkeys(self):
        return {
            'd': self.only_done,
            'u': self.only_undone,
            'a': self.all
        }

    def only_done(self):
        self.mode = 'done'

    def only_undone(self):
        self.mode = 'undone'

    def all(self):
        self.mode = 'all'




