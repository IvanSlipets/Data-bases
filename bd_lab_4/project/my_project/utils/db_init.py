from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()

class BaseSchema(Schema):
    """Базова схема для DTO об'єктів."""
    pass