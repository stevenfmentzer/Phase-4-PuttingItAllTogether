from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class MakeupItem(db.Model, SerializerMixin):
    __tablename__ = 'makeup_items'

    serialize_rules = ('-stores_item.item',)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    brand = db.Column(db.String)
    type = db.Column(db.String)

    stores_item = db.relationship('StoreHasItem', back_populates = 'item')

class Store(db.Model, SerializerMixin):
    __tablename__ = 'stores'

    serialize_rules = ('-item_stores.store',)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

    item_stores = db.relationship('StoreHasItem', back_populates = 'store')

class StoreHasItem(db.Model, SerializerMixin):
    __tablename__ = 'store_has_item'

    serialize_rules = ('-store_has_item','-store.item_stores')

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer)

    item_id = db.Column(db.Integer, db.ForeignKey('makeup_items.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    item = db.relationship('MakeupItem', back_populates = 'stores_item')
    store = db.relationship('Store', back_populates = 'item_stores')