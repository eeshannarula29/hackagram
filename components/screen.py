"""The file contains the View class, which is the super class for all the views/screens of the app"""

from __future__ import annotations

import os
import sys

from typing import Any, Optional

from firebase_manager.handler import Handler


class View:

    def __init__(self, parent: Optional[View] = None, handler: Optional[Handler] = None) -> None:
        # Raise an error if both parent and handler are not provided
        if not parent and not handler:
            raise HandlerNotProvidedError
        # if handler is provided then set self.handler to handler
        if handler:
            self.handler = handler
        # else set self.handler to parents handler
        else:
            self.handler = parent.handler
        # finally set self.parent to parent
        self.parent = parent

    def show(self) -> Optional[str]:
        """Return the content of the view"""
        raise NotImplementedError

    def inquire(self) -> Optional[Any]:
        """Return the option the user choose"""
        raise NotImplementedError

    def get_child(self) -> Optional[View]:
        """Return the child view (uses self.inquire)"""
        raise NotImplementedError


def clear_screen() -> None:
    """clear the terminal screen"""
    if sys.platform == 'darwin' or sys.platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')


def screen_size() -> tuple[int, int]:
    """Return the size of the screen"""
    size = os.get_terminal_size()
    return size.lines, size.columns


class HandlerNotProvidedError(Exception):
    def __str__(self) -> str:
        return 'No handler was provide while initialization of a view'
