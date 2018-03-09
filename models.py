"""Модели"""

from datetime import date, timedelta

class Habit():
    """Привычка"""

    def __init__(self, config_obj, store):
        self.config = config_obj
        self.name = config_obj['name']
        self.tag = config_obj['tag']
        self.code = config_obj['name']
        self.store = store

    def per_interval(self):
        """Сколько событий за интервал"""
        return int(self.config['interval'].split('/')[0])

    def interval_length(self):
        """Длина интервала"""
        return int(self.config['interval'].split('/')[1])

    def interval_for_print(self):
        """Вывести интервал для печати"""
        candidate = self.config.get('interval', '7/7')
        if candidate != '7/7':
            return candidate
        return ''

    def stats(self):
        """Получить статистику"""
        results = []
        today = today_date()
        for i in range(0, 30):
            day = today - timedelta(days=i)
            stats = get_stats_for(self, day)
            if stats:
                results.append(stats)
            elif self.reached_limit(day):
                results.append({'code': 'auto'})
            else:
                results.append(None)
        return results


    def reached_limit(self, day=None):
        """Достигнут недельный лимит"""
        if 'interval' not in self.config:
            return False
        if day is None:
            day = today_date()
        stats = [get_stats_for(self, day - timedelta(days=i))
                 for i
                 in range(0, self.interval_length()-1)]
        return len([s for s in stats if s]) >= self.per_interval()

    def is_ok(self):
        """Выполнено ли на сегодня?"""
        if get_stats_for(self, today_date()):
            return True
        if self.reached_limit():
            return True
        return False


    def skip(self):
        """Пропустить это"""
        self.store.data.append({'code': self.code, 'date': str(today_date()), 'skip': True})

    def toggle(self):
        """Переключить состояние у привычки на текущую дату"""
        if self.is_ok():
            self.remove_today()
        else:
            self.store.data.append({'code': self.code, 'date': str(today_date())})

    def done(self):
        """Пометить выполненным"""
        self.store.data.append({'code': self.code, 'date': str(today_date())})

    def undone(self):
        """Развыполнить"""
        self.remove_today()

    def remove_today(self):
        """Удалить из истории сегодняшнюю запись"""
        for log in self.store.data:
            if log['code'] == self.code:
                if log['date'] == str(today_date()):
                    self.store.data.remove(log)





DATE = None
def today_date():
    """Дата, над которой мы сейчас работаем"""
    global DATE

    if DATE:
        return DATE

    return date.today()


def get_stats_for(habit, day):
    """Получить статистику за дату"""
    for log in habit.store.data:
        if log['code'] == habit.code:
            if log['date'] == str(day):
                return log
    return None
