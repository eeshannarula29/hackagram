class SignInError(Exception):
    def __str__(self) -> str:
        return 'There was an error signing in'


class SignUpError(Exception):
    def __str__(self) -> str:
        return 'There was an error signing up'


class RefreshError(Exception):
    def __str__(self) -> str:
        return 'There was an error while refreshing the token'


class TokenError(Exception):
    def __str__(self) -> str:
        return 'There was can error while using the token'


class InvalidToken(Exception):
    def __str__(self) -> str:
        return 'token and refresh token does not exist'


class HandlerNotProvidedError(Exception):
    def __str__(self) -> str:
        return 'No handler was provide while initialization of a view'
