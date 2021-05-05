"""File contains Loading View class"""

from pyfiglet import figlet_format

from components.progress_bar import *
from components.screen import *
import time

LOGO = figlet_format('HACKAGRAM')
LOGO_ARRAY = LOGO.split('\n')


class LoadingView(View):
    """The class represents a loading screen view"""

    def __init__(self, parent: Optional[View] = None, handler: Optional[Handler] = None, child: Optional[View] = None):
        super().__init__(parent, handler, child)
        self.progress = ProgressBar(len(LOGO_ARRAY[0]))

    def show(self) -> Optional[str]:
        string_so_far = ''
        size = screen_size()

        for row in range(size[0]):
            if row != size[0] // 2:
                string_so_far += '\n'
            else:
                indent = size[1] // 2 - len(LOGO_ARRAY[0]) // 2

                for text_row in LOGO_ARRAY:
                    string_so_far += ' ' * indent + text_row + '\n'
                string_so_far += ' ' * indent + self.progress.get_bar()

        return string_so_far

    def inquire(self) -> Optional[Any]:
        return None

    def present(self) -> Optional[View]:

        while self.progress.progress_percentage != 100.0:
            clear_screen()
            print(self.show())
            self.progress.increment()
            time.sleep(.1)

        return self.next if self.next else self.inquire()
