"""Вспомогательные функции"""

from getch import char_input
import command
import mode

GLOBAL_HOTKEYS = {
    '$legend': '$',
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
    action = GLOBAL_HOTKEYS[answer]
    if isinstance(action, dict):
        second_answer = char_input(action['$legend']+': ')
        print()
        if second_answer in action:
            action = action[second_answer]
        else:
            return None
    return action(store)

def repl_loop(store, screen):
    """Запустить работу над экраном"""
    print('>>>Loop started')
    while True:
        print('>>>   Loop iteration')
        screen.print()
        answer = char_input()
        if screen.respondsto(answer):
            maybe_screen = screen.doaction(answer)
            if not maybe_screen:
                break
            else:
                screen = maybe_screen
        if have_global_action(answer):
            maybe_screen = do_global_action(answer, store)
            if maybe_screen:
                screen = maybe_screen
