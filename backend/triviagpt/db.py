from sqlalchemy import create_engine

engine = None


def get_sql_alchemy_engine():
    return engine


def init(app):
    """
    Initialize the engine.
    """
    global engine
    engine = create_engine(
        f"postgresql://{app.config['DATABASE_USER']}:{app.config['DATABASE_PASSWORD']}@{app.config['DATABASE_HOST']}:{app.config['DATABASE_PORT']}/{app.config['DATABASE_NAME']}"
    )