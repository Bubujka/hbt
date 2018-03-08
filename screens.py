"""Определение экранов в приложении"""
class Screen():

    def __init__(self, store):
        self.store = store

    def respondsto(self, answer):
        return answer in self.hotkeys()

    def do(self, answer):
        self.hotkeys()[answer]()

    def hotkeys(self):
        return {}



class OneByOneScreen(Screen):
    pass

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




