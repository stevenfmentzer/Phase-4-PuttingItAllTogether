from app import app

from models import db, MakeupItem, Store, StoreHasItem

if __name__ == '__main__':
    with app.app_context():
        pass