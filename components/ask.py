from PyInquirer import prompt
from typing import Optional, Any

# some default options
EXIT = 'Exit'
LOGOUT = 'Logout'


class Question:

    def __init__(self, message: Optional[str] = '') -> None:
        self.question = {'message': message, 'name': 'answer'}

    def ask(self) -> Optional[Any]:
        raise NotImplementedError

    def update(self, d: dict) -> None:
        self.question.update(d)


class InputQuestion(Question):

    def __init__(self, message: Optional[str] = '') -> None:
        super().__init__(message)
        self.update({'type': 'input'})

    def ask(self) -> Optional[Any]:
        return prompt(self.question).get('answer', None)


class PasswordQuestion(Question):

    def __init__(self, message: Optional[str] = '') -> None:
        super().__init__(message)
        self.update({'type': 'password'})

    def ask(self) -> Optional[Any]:
        return prompt(self.question).get('answer', None)


class ListQuestion(Question):

    def __init__(self, message: Optional[str] = '', choices: Optional[list] = None) -> None:
        super().__init__(message)
        self.update({'type': 'list', 'choices': choices if choices else []})

    def ask(self) -> Optional[Any]:
        return prompt(self.question).get('answer', None)

    def add_choice(self, element: Any) -> None:
        self.question['choices'].append(element)

    def add_choices(self, choices: list) -> None:
        self.question['choices'].extend(choices)


class CheckBoxQuestion(Question):

    def __init__(self, message: Optional[str] = '', choices: Optional[list] = None) -> None:
        super().__init__(message)
        self.update({'type': 'checkbox', 'choices': choices if choices else []})

    def ask(self) -> Optional[Any]:
        return prompt(self.question).get('answer', None)

    def add_choice(self, element: Any) -> None:
        self.question['choices'].append({'name': element})

    def add_choices(self, choices: list) -> None:
        self.question['choices'].extend([{'name': element} for element in choices])
