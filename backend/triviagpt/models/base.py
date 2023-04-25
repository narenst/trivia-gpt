from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    """
    Mixin class for all models.
    Includes CRUD operations.
    """
    pass
    