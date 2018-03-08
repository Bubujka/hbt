"""Определение экранов в приложении"""

import lib
import mode
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
        self.habits = ['one', 'two', 'three', 'four']
        self.index = 0

    def print(self):
        if self.index == len(self.habits):
            return mode.summary(self.store)
        lib.repl_loop(
                self.store,
                HabitScreen(self.store, self.habits[self.index]))
        self.index += 1
        self.print()






class HabitScreen(Screen):
    def __init__(self, store, habit):
       super(HabitScreen, self).__init__(store)
       self.habit = habit

    def print(self):
        print(self.habit)

    def hotkeys(self):
        return {
            'l': self.later,
            's': self.skip,
            'd': self.done
        }

    def later(self):
        print('later')
        return False

    def skip(self):
        print('skip')
        return False

    def done(self):
        print('done')
        return False





class SummaryScreen(Screen):
    def hotkeys(self):
        return {
            'a': self.say_a,
            'b': self.say_b
        }

    def say_a(self):
        print('aaaaaaaaaaaa')

    def say_b(self):
        print('bbbbbbbbbbb')




