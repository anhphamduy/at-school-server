from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os

SCOPES = 'https://mail.google.com/'
DIR_ = "app/controllers/email/"


def auth(token_):
    """ Authenticates user from a token.json file enabling
            get request from the Google APIs """
    store = file.Storage(
        f"{os.getcwd()}/app/controllers/email/tokens/{token_}.json")
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(
            DIR_+'client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return build('gmail', 'v1', http=creds.authorize(Http()))
