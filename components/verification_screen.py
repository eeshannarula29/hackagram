from components.screen import *
from components.ask import *

MAIL = "📬"


class VerificationView(View):

    def show(self) -> Optional[str]:
        return render_logo()

    def inquire(self) -> Optional[View]:

        if self.handler.auth.get_user_info(self.handler.token)['users'][0]['emailVerified']:
            return None

        else:
            question = ListQuestion("Please verify your account with the verification link sent to your email address", ['Refresh', 'Exit'])
            question.update({'qmark': MAIL})

            answer = question.ask()

            if answer == 'Refresh':
                return self

            elif answer == 'Exit':
                return self.parent.parent

            else:
                return self

    def present(self) -> Optional[View]:
        clear_screen()
        print(self.show())
        self.next = self.inquire()
        return self.next
