#!/usr/bin/env python3
import time
import random
import os
import subprocess
import shutil

def pipi():
    pipi_default = "(• ‿ •)"
    pipi_surprise = "(• o •)"
    pipi_blink = "(— ‿ —)"
    pipi_sleep = "( — . — )"
    pipi_listen = "(d[• ‿ •]b)"

    playerctl_exists = shutil.which("playerctl") is not None
    player_status = ""

    if playerctl_exists:
        try:
            status = subprocess.run(
                ["playerctl", "status"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=1
            )
            player_status = status.stdout.strip()
        except Exception:
            player_status = ""

    now = time.localtime()
    sleep_time = now.tm_hour >= 23 or now.tm_hour <= 7

    if os.environ.get('BLOCK_BUTTON'):
            return pipi_surprise

    if sleep_time:
            return pipi_sleep

    if player_status.lower() == "playing":    
            return pipi_listen
        
    if random.randint (1, 30) == 1:
            return pipi_blink
    return pipi_default
        

if __name__ == "__main__":
    print(pipi())