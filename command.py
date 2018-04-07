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

def prepend_to_plan_md(store):
    """Добавить список несделанного в план"""
    ok_items = [h for h in store.habits() if not h.is_ok()]
    text = "\n# Habbit plan\n"
    text += ("\n".join("- " +h.name for h in ok_items))
    text += "\n\n"
    plan = open(expanduser('~/.db/wiki/plan.md')).read();
    open(expanduser('~/.db/wiki/plan.md'), 'w').write(text+plan)
    call(['open-in-gvim', expanduser('~/.db/wiki/plan.md')])


