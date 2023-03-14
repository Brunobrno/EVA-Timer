import time, os, sys

from colorama import init, Fore, Back, Style

def yellow_background():
    print(Back.YELLOW, end='')

print(Style.RESET_ALL, end='')
print("hello", end=' ')
yellow_background()
print("world", end='')
