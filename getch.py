"""Модуль для взаимодействия с клавиатурой"""

import sys
import termios
import tty

def getch():
    """Get a single character from stdin, Unix version\nhttps://gist.github.com/payne92/11090057"""
    stdin = sys.stdin.fileno()
    old_settings = termios.tcgetattr(stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(stdin, termios.TCSADRAIN, old_settings)
    return char

def char_input(prompt="$ "):
    """Получить 1 символ от человека"""
    print(prompt, end="", flush=True)
    return getch()
