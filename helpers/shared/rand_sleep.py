import time
from random import choice

from colorama import Fore


def rand_sleep(start=1, end=2):
    r = range(start, end)
    rand_num = choice(r)
    print(Fore.YELLOW + f'--sleep-- {rand_num}' + Fore.RESET)

    time.sleep(rand_num)
