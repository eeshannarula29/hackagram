"""File controls the application while it is running"""

import time

from components.loding_screen import *
from firebase_manager.handler import Handler
from keys import keys


def run() -> None:
    start_time = time.time()
    threshold_time = 15 * 60  # 15 minutes in secs
    handler = Handler(keys.keys_auth, keys.keys_database)
    curr_view = LoadingView(handler=handler)

    while curr_view:
        current_time = time.time()
        time_diff = current_time - start_time

        if threshold_time < time_diff:
            handler.refresh()
            start_time = time.time()

        curr_view = curr_view.present()


if __name__ == '__main__':
    run()
