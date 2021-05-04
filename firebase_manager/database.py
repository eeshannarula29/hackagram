"""File contains the Database class used to get set and delete data for a user"""

from typing import Any, Optional

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from firebase_admin.exceptions import FirebaseError

# name of the collection in the cloud storage
COLLECTION = 'users'


# data stored in the cloud for a new user
def get_new_user(email: str) -> dict:
    return {
        'email': email,
        'followers': [],
        'following': [],
        'requests_sent': [],
        'requests_received': []
    }


class Database:
    """Handles the cloud storage"""
    def __init__(self, key: str) -> None:
        self.cred = credentials.Certificate(key)
        self.app = firebase_admin.initialize_app(self.cred)

        self.db = firestore.client()  # this object is the connection between the cloud and the app

    def set_document(self, email: str, update: Optional[bool] = False) -> Any:
        try:
            # - db here is the cloud storage
            # - in the storage we are creating a collection (of documents)
            # - each document represents a users data
            # - we will be identifying the document in the collection by the email of the user
            return self.db.collection(COLLECTION).document(email).set(get_new_user(email), merge=update)
        # if there was any error return None
        except (ValueError, TypeError, FirebaseError):
            return None

    def get_document(self, email: str) -> Any:
        try:
            # refer to the document with id:email and use get() method on it
            return self.db.collection(COLLECTION).document(email).get().to_dict()
        # if there was any error return None
        except FirebaseError:
            return None

    def delete_document(self, email: str) -> Any:
        try:
            # refer to the document with id:email and use delete() method on it
            return self.db.collection(COLLECTION).document(email).delete()
        # if there was any error return None
        except FirebaseError:
            return None
