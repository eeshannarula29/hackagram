from components.screen import *
from components.ask import *
from exc import *


SKULL = "☠️"


class RegisterView(View):

    def show(self) -> Optional[str]:
        return render_logo()

    def inquire(self) -> Optional[View]:
        email_question = InputQuestion("Enter your email address:")
        password_question = PasswordQuestion("Enter new Password:")

        email = email_question.ask()
        password = password_question.ask()

        try:
            self.handler.register(email, password)
            self.handler.auth.send_verification(self.handler.token)
            
            return None

        except SignUpError:
            print(f'\n {SKULL} The email or the password is incorrect \n')

            try_again_question = ListQuestion("Do you want to:", ['Try Again', 'Exit'])
            try_again_answer = try_again_question.ask()

            if try_again_answer == 'Try Again':
                self.inquire()

            elif try_again_answer == 'Exit':
                return self.parent

            else:
                return self

    def present(self) -> Optional[View]:
        clear_screen()
        print(self.show())
        return self.inquire()
