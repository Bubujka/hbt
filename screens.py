"""Определение экранов в приложении"""
class Screen():
    """Класс экрана"""
    def __init__(self, store):
        self.store = store

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




