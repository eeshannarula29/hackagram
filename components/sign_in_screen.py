from components.verification_screen import *
from components.screen import *
from components.ask import *
from exc import *

SKULL = "☠️"


class SignInView(View):

    def inquire(self) -> Optional[View]:
        email_question = InputQuestion("Enter your registered Email address:")
        password_question = PasswordQuestion("Enter the password:")

        email = email_question.ask()
        password = password_question.ask()

        try:
            self.handler.sign_in(email, password)

            return VerificationView(parent=self)

        except SignInError:
            print(f'\n {SKULL} The email or the password is incorrect \n ')

            try_again_question = ListQuestion("Do you want to:", ['Try Again', 'Exit'])
            try_again_answer = try_again_question.ask()

            if try_again_answer == 'Try Again':
                self.inquire()

            elif try_again_answer == 'Exit':
                return self.parent

            else:
                return self
