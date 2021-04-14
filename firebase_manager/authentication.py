from typing import Any

import pyrebase
from requests.exceptions import HTTPError

from validate_email import validate_email


class Auth:
    """Used to authenticate a user using firebase authenticate services"""

    def __init__(self, keys: dict) -> None:
        self.app = pyrebase.initialize_app(keys)
        self.auth = self.app.auth()

    def create_user(self, email: str, password: str) -> Any:
        try:
            # calling pyrebase's create_user_with_email_and_password function
            return self.auth.create_user_with_email_and_password(email, password)
        # handle the exception thrown by pyrebase
        except HTTPError:
            return None

    def sign_in(self, email: str, password: str) -> Any:
        try:
            # calling pyrebase's sign_in_with_email_and_password function
            return self.auth.sign_in_with_email_and_password(email, password)
        # handle the exception thrown by pyrebase
        except HTTPError:
            return None

    def get_user_info(self, id_token) -> Any:
        try:
            # calling pyrebase's get_account_info function
            return self.auth.get_account_info(id_token)
        # handle the exception thrown by pyrebase
        except HTTPError:
            return None

    def is_user(self, id_token: Any) -> bool:
        try:
            # try to retrieve the data of a user
            self.auth.get_account_info(id_token)
            # return true if successful
            return True
        # else handle the exception and return false
        except HTTPError:
            return False

    def delete_user(self, id_token: Any) -> Any:
        try:
            # calling pyrebase's delete_user_account function
            return self.auth.delete_user_account(id_token)
        # handle the exception thrown by pyrebase
        except HTTPError:
            return None

    def validate_email(self, email: str) -> bool:
        return validate_email(email)

    def send_verification(self, id_token: Any) -> Any:
        try:
            return self.auth.send_email_verification(id_token)
        except HTTPError:
            return None

    def send_reset_password(self, id_token) -> Any:
        try:
            return self.auth.send_password_reset_email(self.get_user_info(id_token)['users'][0]['email'])
        except HTTPError:
            return None

    def refresh_token(self, refresh_token: Any) -> Any:
        try:
            return self.auth.refresh(refresh_token)
        except HTTPError:
            return None
