"""Хранилище, состояние"""

from os.path import expanduser
import json

from colorama import ansi

from getch import char_input
import lib
import models


DATA_FILE = expanduser("~/.db/wiki/habits.json")

class RerenderEvent(Exception):
    """Событие перерисовки экрана"""
    pass

def clear_screen():
    """Зачистить экран"""
    print(ansi.clear_screen())

def input_legend_for(screen):
    screenhotkeys = "".join(screen.hotkeys().keys())
    globalhotkeys = "".join(lib.GLOBAL_HOTKEYS.keys() - ['$legend'])

    return "$ ["+screenhotkeys +' '+ globalhotkeys+"]: "


class Store():
    """Хранилище данных и экрана"""
    def __init__(self):
        self.windows = []
        self.data = json.loads(open(DATA_FILE).read())

    def rerender(self):
        """Перерисовать экран"""
        raise RerenderEvent()

    def habits(self):
        return [models.Habit(c, self) for c in lib.cfg()['items']]

    def back(self):
        """Вернуться на предыдущий экран"""
        del self.windows[-1]
        self.rerender()

    def add_window(self, window):
        self.windows.append(window)


    def render(self):
        """Отрендерить последний экран, выполнить действие в его контексте"""
        while True:
            try:
                #print(self.windows)
                clear_screen()
                screen = self.windows[-1]
                screen.print()
                answer = char_input(input_legend_for(screen))
                if screen.respondsto(answer):
                    screen.doaction(answer)
                if lib.have_global_action(answer):
                    lib.do_global_action(answer, self)
            except RerenderEvent:
                pass

    def save(self):
        open(DATA_FILE, 'w').write(json.dumps(self.data, indent=2))



