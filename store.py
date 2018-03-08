"""Хранилище, состояние"""

from getch import char_input
import lib

class RerenderEvent(Exception):
    pass

class Store():
    def __init__(self):
        self.windows = []

    def rerender(self):
        raise RerenderEvent()

    def back(self):
        del self.windows[-1]
        self.rerender()

    def add_window(self, window):
        self.windows.append(window)


    def render(self):
        """Отрендерить последний экран, выполнить действие в его контексте"""
        while True:
            try:
                print(self.windows)
                screen = self.windows[-1]
                screen.print()
                answer = char_input()
                if screen.respondsto(answer):
                    screen.doaction(answer)
                if lib.have_global_action(answer):
                    lib.do_global_action(answer, self)
            except RerenderEvent:
                pass


    def save(self):
        pass


