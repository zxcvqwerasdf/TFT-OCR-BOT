"""
Where the bot execution starts & contains the game loop that keeps the bot running indefinitely
"""

import multiprocessing
from ui import UI
import auto_queue
from game import Game
import settings
import auto_comps
from comps import CompsManager

def game_loop(ui_queue: multiprocessing.Queue, comps : CompsManager)  -> None:
    """Keeps the program running indefinetly by calling queue and game start in a loop"""
    while True:
        auto_queue.queue()
        Game(ui_queue, comps)


if __name__ == "__main__":
    if settings.LEAGUE_CLIENT_PATH is None:
        raise Exception(
            "No league client path specified. Please set the path in settings.py")
    comps_manager = CompsManager()
    message_queue = multiprocessing.Queue()
    overlay: UI = UI(message_queue)
    game_thread = multiprocessing.Process(target=game_loop, args=(message_queue,comps_manager))

    print("TFT OCR | https://github.com/jfd02/TFT-OCR-BOT")
    print("Close this window to terminate the overlay window & program")
    auto_comps.LoadChampionsAndComps(comps_manager)
    game_thread.start()
    overlay.ui_loop()
