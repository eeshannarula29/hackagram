"""The file contains the sign view which would give the user option to sign in or sign up to the app

Cheatsheet for emojis: https://unicode.org/emoji/charts/emoji-list.html
"""
from components.register_screen import *
from components.screen import *
from components.ask import *


WAVE = '\U0001F44B'  # 👋
SMILEY = '\U0001f600'  # 😀


class SignView(View):

    def show(self) -> Optional[str]:
        return render_logo()

    def inquire(self) -> Optional[View]:

        question = ListQuestion(f'Hi {WAVE}, Please Sign In or Register', ['Register', 'SignIn', 'Quit'])

        question.update({'qmark': SMILEY})
        answer = question.ask()

        if answer == 'Quit':
            clear_screen()
            return None

        elif answer == 'Register':
            return RegisterView(parent=self)

        elif answer == 'SignIn':
            return None

        else:
            return self

    def present(self) -> Optional[View]:
        clear_screen()
        print(self.show())
        return self.inquire()
