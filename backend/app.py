import os
import uuid

from flask import Flask, request, jsonify, redirect
from supabase import create_client, Client
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from flask_cors import CORS

load_dotenv()

url: str = os.environ.get("SUPRABASE_URL")
key: str = os.environ.get("SUPRABASE_KEY")

if not url or not key:
    raise ValueError("Suprabase URL and Key must be set in the .env file")

supabase: Client = create_client(url, key)

app = Flask(__name__)

CORS(app)

FILES_TABLE = 'files'
STORAGE_BUCKET = 'uploads'

@app.route('/')
def index():
    """Confirms the server is running"""
    return "Content delivery app is running"