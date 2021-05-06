"""File contains Handler class which handles the Auth and Database classes
to handle the users of the app"""

from firebase_manager.authentication import Auth
from firebase_manager.database import Database

from exc import *


class Handler:
    def __init__(self, keys_auth: dict, keys_database: str):

        self.auth = Auth(keys_auth)
        self.database = Database(keys_database)

        self._token = None
        self._refresh_token = None

    def register(self, email: str, password: str) -> None:
        # try to create a user from
        user_info = self.auth.create_user(email, password)
        # if user is created assign the tokens
        if user_info:
            self._token = user_info['idToken']
            self._refresh_token = user_info['refreshToken']
            # and create a storage for this user
            self.database.set_document(email)
        # else failed to create a user
        else:
            raise SignUpError

    def sign_in(self, email: str, password: str) -> None:
        # try to sign in with the email and password
        user_info = self.auth.sign_in(email, password)
        # did log in
        if user_info:
            # set the token and refresh token
            self._token = user_info['idToken']
            self._refresh_token = user_info['refreshToken']
        # error while logging in
        else:
            raise SignInError

    def refresh(self) -> None:
        # If there is no token
        if not self._token or not self._refresh_token:
            raise InvalidToken
        # refresh the tokens
        new_data = self.auth.refresh_token(self._refresh_token)
        # if the new token was generated
        if new_data:
            self._token = new_data['idToken']
            self._refresh_token = new_data['refreshToken']
        # else there was an error while refreshing
        else:
            raise RefreshError

    def delete_account(self, email) -> None:

        # If there is no token
        if not self._token or not self._refresh_token:
            raise InvalidToken

        # Get the info of the user with self._token
        user_info = self.auth.get_user_info(self._token)

        # if token expired or invalid token
        if not user_info:
            raise TokenError

        # if email is not matching the retrieved user_info's email
        if not user_info['users'][0]['email'] != email:
            raise ValueError("the email provided is different from current session's email")

        # If no error was raised then delete the account
        self.auth.delete_user(self._token)
        self.database.delete_document(email)

    @property
    def token(self) -> str:
        return self._token
