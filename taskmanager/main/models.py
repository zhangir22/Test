from django.db import models
from django.db import transaction
import requests
import logging
import os
from datetime import datetime
from typing import Optional, Tuple

import jwt
import requests


class Contact(models.Model):
    name = models.TextField("Название")
    email = models.TextField("Почта")
    phone = models.TextField("Телефон")

    def __str__(self):
        return str(self.name)+" - "+str(self.email)


class TokensStorage(models.Model):
    def get_access_token(self) -> Optional[str]:
        pass

    def get_refresh_token(self) -> Optional[str]:
        pass

    def save_tokens(self, access_token: str, refresh_token: str):
        pass


class MemoryTokensStorage(TokensStorage):


    def __init__(self):
        self._access_token = None
        self._refresh_token = None

    def get_access_token(self) -> Optional[str]:
        return self._access_token

    def get_refresh_token(self) -> Optional[str]:
        return self._refresh_token

    def save_tokens(self, access_token: str, refresh_token: str):
        self._access_token, self._refresh_token = access_token, refresh_token

