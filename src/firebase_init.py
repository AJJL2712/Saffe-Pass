import firebase_admin
from firebase_admin import credentials, firestore, auth
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "firebase_config.json")

cred = credentials.Certificate(CONFIG_PATH)
firebase_admin.initialize_app(cred)

db = firestore.client()
