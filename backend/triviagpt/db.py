from flask_sqlalchemy import SQLAlchemy

engine = None
db = SQLAlchemy()

def get_sql_alchemy_engine():
    return engine


def get_sql_alchemy_db():
    return db


def init(app):
    """
    Initialize the engine.
    """
    global db
    sqlalchemy_database_uri = f"postgresql://{app.config['DATABASE_USER']}:{app.config['DATABASE_PASSWORD']}@{app.config['DATABASE_HOST']}:{app.config['DATABASE_PORT']}/{app.config['DATABASE_NAME']}"
    app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_database_uri
    db.init_app(app)