"""File controls the application while it is running"""
from components.loding_screen import *
from firebase_manager.handler import Handler
from keys import keys


def run() -> None:
    handler = Handler(keys.keys_auth, keys.keys_database)
    curr_view = LoadingView(handler=handler)

    while curr_view:
        curr_view = curr_view.present()


if __name__ == '__main__':
    run()
