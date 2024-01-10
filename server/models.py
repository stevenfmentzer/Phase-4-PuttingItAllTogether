from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class MakeupItem(db.Model, SerializerMixin):
    pass

class Store(db.Model, SerializerMixin):
    pass

class StoreHasItem(db.Model, SerializerMixin):
    pass