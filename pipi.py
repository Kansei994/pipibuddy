#!/usr/bin/env python3
import time
import random
import os

def pipi():
    pipi_default = "(• ‿ •)"
    pipi_surprise = "(• o •)"
    pipi_blink = "(— ‿ —)"
    pipi_sleep = "( — . — )"

    now = time.localtime()
    sleep_time = now.tm_hour >= 23 or now.tm_hour <= 7

    if os.environ.get('BLOCK_BUTTON'):
        return pipi_surprise
    elif sleep_time:
        return pipi_sleep
    else: return pipi_blink if random.randint(0,3) == 0 else pipi_default 

if __name__ == "__main__":
    print(pipi())