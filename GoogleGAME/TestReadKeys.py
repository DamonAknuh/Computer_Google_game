import tty
import termios
import sys
import os
import time


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    s = ch.encode('utf-8')

    return s.hex()


while True:
    s = getch()
    if s == "20":
        print ("Up")
    elif s == "1b":
        print("SHIIITT")
    elif s == "70":
        break
