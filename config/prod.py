import os

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_PROD")
SQLALCHEMY_TRACK_MODIFICATIONS = False