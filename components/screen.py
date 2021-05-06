"""The file contains the View class, which is the super class for all the views/screens of the app"""

from __future__ import annotations

import os
import sys

from typing import Any, Optional

from firebase_manager.handler import Handler
from pyfiglet import figlet_format

from exc import HandlerNotProvidedError

LOGO = figlet_format('HACKAGRAM')
LOGO_ARRAY = LOGO.split('\n')


class View:
    """Represents a screen/view on the app

    Attribute Instances:
    - parent: the parent view object from which self was presented
    - child: the child view which self would throw as the next screen
    - handler: the handler used to handle the user

    Note: if a parent is provided then there is no need to provide a handler, but one of
    them needs to be provided.
    """

    def __init__(self, parent: Optional[View] = None, handler: Optional[Handler] = None, child: Optional[View] = None) -> None:
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
        # set up the next screen
        self.next = child

    def show(self) -> Optional[str]:
        """Return the content of the view"""
        return render_logo()

    def inquire(self) -> Optional[View]:
        """Return the view corresponding to option the user choose"""
        raise NotImplementedError

    def present(self) -> Optional[View]:
        """present self in the app and Return the child view (uses self.inquire)"""
        clear_screen()
        print(self.show())
        self.next = self.inquire()
        return self.next


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


def render_logo() -> str:
    """Return string representation of logo of the app"""
    string_so_far = '\n'
    size = screen_size()

    indent = size[1] // 2 - len(LOGO_ARRAY[0]) // 2

    for text_row in LOGO_ARRAY:
        string_so_far += ' ' * indent + text_row + '\n'

    return string_so_far
