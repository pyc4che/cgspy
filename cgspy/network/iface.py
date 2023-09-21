from random import choice
from netifaces import interfaces


def choose():
    return choice(
        interfaces()
    )
