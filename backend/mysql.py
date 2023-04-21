import os
from flask_sqlalchemy import SQLAlchemy


def setup(app):
    db_user = os.environ["DB_USER"]
    db_pass = os.environ["DB_PASS"]
    db_host = os.environ["DB_HOST"]
    db_port = os.environ["DB_PORT"]
    db_name = os.environ["DB_NAME"]
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    db = SQLAlchemy(app)
    return db
