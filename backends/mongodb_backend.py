import exceptions.mvc_exceptions as mvc_exc
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

DB_NAME = 'products'
COLLECTION_NAME = 'items'

products_collection = None


def connect_to_db(db=None):
    global products_collection

    # TODO: Implementar conexoes diferentes de localhost
    if db is None:
        print('Connecting to MongoDB localhost...')
        try:
            client = MongoClient(serverSelectionTimeoutMS=2000)
            products_collection = client[DB_NAME][COLLECTION_NAME]
        except ServerSelectionTimeoutError as e:
            print("Can't connect to MongoDB server")
    else:
        pass


def create_table(table_name):
    pass


def insert_one(name, price, quantity, table_name):
    result = products_collection.find_one({'name': name})
    if result is None:
        products_collection.insert_one(
            {
                'name': name,
                'price': price,
                'quantity': quantity
            }
        )
    else:
        raise mvc_exc.ItemAlreadyStored(
            # TODO: Verificar se alguma excecao ocorre
            # f'{e}: "{name}"" already stored in table "{table_name}"'
            f'"{name}"" already stored in table "{table_name}"'
        )


def insert_many(items, table_name):
    for item in items:
        result = products_collection.find_one({'name': item['name']})
        if result is None:
            products_collection.insert_one(
                {
                    'name': item['name'],
                    'price': item['price'],
                    'quantity': item['quantity']
                }
            )


def select_one(item_name, table_name):
    result = products_collection.find_one({'name': item_name})
    if result is not None:
        return result
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't read '{item_name}' because it's not stored in table '{table_name}'")


def select_all():
    result = []
    for prod in products_collection.find():
        result.append(prod)
    return result


def update_one(name, price, quantity, table_name):
    result = products_collection.find_one({'name': name})
    if result is not None:
        products_collection.update(
            {'name': name},
            {'$set':
                {
                    'price': price,
                    'quantity': quantity
                }
             }
        )
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't update '{name}' because it's not stored in table '{table_name}'")


def delete_one(name, table_name):
    result = products_collection.find_one({'name': name})
    if result is not None:
        products_collection.delete_one({'name': name})
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't delete '{name}' because it's not stored in table '{table_name}'")
