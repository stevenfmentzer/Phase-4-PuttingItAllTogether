# Phase-4-PuttingItAllTogether

1. Fill out the DB models as per the DB schema.
2. Add relationships and serialization rules to the models.
    - Make sure that a store's name is a string greater than 0 characters.
    - Also make sure that the price of a store/item is a positive number.
3. Add GET routes to `/makeup_items`, `/stores`, `/stores/<int:id>`
4. Add DELETE route to `/stores/<int:id>`
5. Add POST route to `/stores`
6. Add PATCH route to `/store_has_item/<int:id>`