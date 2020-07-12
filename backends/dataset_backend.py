import dataset
from sqlalchemy.exc import NoSuchTableError, IntegrityError
from exceptions import mvc_exceptions as mvc_exc

DB_name = 'myDB'


def connect_to_db(db=None):
    if db is None:
        mydb = ':memory:'
        print('New connection to in-memory SQLite DB...')
    else:
        mydb = f'{db}.db'
        print('New connection to SQLite DB...')
    connection = dataset.connect(f'sqlite:///{mydb}')
    return connection


def create_table(conn, table_name):
    try:
        table = conn.get_table(table_name)
    except Exception as e:
        print(f"Table {table_name} does not exist. It will be created now")
        conn.get_table(table_name, primary_id='name', primary_type='String')
        print(f"Created table {table_name} on database {DB_name}")


def insert_one(conn, name, price, quantity, table_name):
    table = conn.load_table(table_name)
    try:
        table.insert(dict(name=name, price=price, quantity=quantity))
    except IntegrityError as e:

        raise mvc_exc.ItemAlreadyStored(
            f'"{name}" already stored in table "{table.table.name}.\nOriginal exception raised: {e}"')


def insert_many(conn, items, table_name):
    table = conn.load_table(table_name)
    try:
        for x in items:
            table.insert(
                dict(name=x['name'], price=x['price'], quantity=x['quantity'])
            )
    except IntegrityError as e:
        print(
            f"At least one in {[x['name'] for x in items]} was already stored in table '{table.table.name}'.\nOriginal exception raised: {e}")
        raise mvc_exc.ItemAlreadyStored(
            f'"{name}" already stored in table "{table.table.name}.\nOriginal exception raised: {e}"')


def select_one(conn, name, table_name):
    table = conn.load_table(table_name)
    row = table.find_one(name=name)
    if row is not None:
        return dict(row)
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't read '{name}' because it's not stored in '{table.table.name}'")


def select_all(conn, table_name):
    table = conn.load_table(table_name)
    return list(map(lambda x: dict(x), table.all()))


def update_one(conn, name, price, quantity, table_name):
    table = conn.load_table(table_name)
    row = table.find_one(name=name)
    if row is not None:
        item = {'name': name, 'price': price, 'quantity': quantity}
        table.update(item, keys=['name'])
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't update '{name}' because it's not stored in  table '{table.table.name}'")


def delete_one(conn, item_name, table_name):
    table = conn.load_table(table_name)
    row = table.find_one(name=item_name)
    if row is not None:
        table.delete(name=item_name)
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't delete '{item_name}' because it's not stored in table '{table.table.name}'")
