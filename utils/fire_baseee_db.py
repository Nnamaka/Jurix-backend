import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

firejson = os.environ['FIREBASE_SERVICE_ACCOUNT']
acct_cert = json.loads(firejson)

if isinstance(acct_cert, dict):
    print('valid')
else: print('invalid data format')

cred = credentials.Certificate(acct_cert)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
    print('firebase app initialized')
else: print('Already initialized firebase app')

db = firestore.client()

