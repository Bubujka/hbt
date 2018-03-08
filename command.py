"""Глобальные команды"""

from os.path import expanduser
from subprocess import call

def save_quit(store):
    """Выйти из программы, сохранив информацию"""
    store.save()
    exit()

def force_quit(_):
    """Выйти из программы не сохраняясь"""
    exit()

def config(_):
    """Открыть редактирование конфига"""
    call(['vim', expanduser('~/.db/wiki/habit-config.json')])
