from config import app
from flask import make_response, request
from flask_restful import Api, Resource

from models import db, MakeupItem, Store, StoreHasItem

api = Api(app)

@app.route('/makeup_items', methods = ['GET'])
def makeup_items():
    makeup_items = MakeupItem.query.all()

    makeup_items_dict = [item.to_dict() for item in makeup_items]

    response = make_response(
        makeup_items_dict, 
        200
    )

    return response

@app.route('/stores', methods = ['GET'])
def stores():
    stores = Store.query.all()

    stores_dict = [store.to_dict(rules = ('-item_stores',)) for store in stores]

    response = make_response(
        stores_dict, 
        200
    )
    return response

@app.route('/store/<int:id>', methods = ['GET','DELETE'])
def store_by_id(id):
    store = Store.query.filter(Store.id == id).first()

    if store:
        if request.method == 'GET':
            response = make_response(
                store.to_dict(), 
                200
            )
        elif request.method == 'DELETE':
            assoc_store_item
    else: 
        response = make_response(
            {"ERROR : STORE NOT FOUND"}, 
            404
        )

    return response


if __name__ == "__main__":
    app.run(port = 5555, debug = True)