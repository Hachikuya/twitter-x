import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

import env
import django
django.setup()

import requests

def get_user_auth_header(consumer_key=None, )
    """
    Follow twitter practice
    'authorization:
        OAuth
        oauth_consumer_key="CONSUMER_API_KEY",
        oauth_nonce="OAUTH_NONCE",
        oauth_signature="OAUTH_SIGNATURE",
        oauth_signature_method="HMAC-SHA1",
        oauth_timestamp="OAUTH_TIMESTAMP",
        oauth_token="ACCESS_TOKEN",
        oauth_version="1.0"
    '
    """
    return

r = requests.get('')