from exceptions import mvc_exceptions as mvc_exc
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric, insert, select, update, delete
from sqlalchemy.exc import IntegrityError

DB_name = 'myDB'

# Inicializacao atraves de connect_to_db()
engine = None

metadata = MetaData()

products = Table(
    'product',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(40), index=True, unique=True, nullable=False),
    Column('price', Numeric(12, 2), nullable=False),
    Column('quantity', Integer(), nullable=False),
)


def connect_to_db(db=None):
    global engine

    if db is None:
        mydb = ':memory:'
        print('New connection to in-memory SQLite DB...')
    else:
        mydb = f'{db}.db'
        print('New connection to SQLite DB...')

    engine = create_engine(f'sqlite:///{mydb}', echo=False)
    connection = engine.connect()
    return connection


def tuple_to_dict(mytuple):
    mydict = dict()
    mydict['id'] = mytuple[0]
    mydict['name'] = mytuple[1]
    mydict['price'] = mytuple[2]
    mydict['quantity'] = mytuple[3]
    return mydict


def create_table():
    metadata.create_all(engine)


def insert_one(conn, name, price, quantity, table_name):
    ins = products.insert().values(
        name=name,
        price=price,
        quantity=quantity
    )
    try:
        conn.execute(ins)
    except IntegrityError as e:
        raise mvc_exc.ItemAlreadyStored(
            f'{e}: "{name}" already stored in table "{table_name}"')


def insert_many(conn, items, table_name):
    ins = products.insert()
    try:
        conn.execute(ins, items)
    except:
        pass


def select_one(conn, item_name, table_name):
    result = conn.execute(
        select([products]).where(products.c.name == item_name)
    ).first()
    if result is not None:
        return tuple_to_dict(result)
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't read '{item_name}' because it's not stored in table '{table_name}'")


def select_all(conn, table_name):
    # TODO: retirar o nome da tabela
    result = []
    for prod in conn.execute(products.select()).fetchall():
        result.append(tuple_to_dict(prod))
    return result


def update_one(conn, name, price, quantity, table_name):
    result = conn.execute(
        select([products]).where(products.c.name == name)
    ).first()
    if result is not None:
        conn.execute(
            update(products).where(products.c.name == name).values(
                price=price,
                quantity=quantity
            )
        )
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't update '{name}' because it's not stored in table '{table_name}'")


def delete_one(conn, name, table_name):
    result = conn.execute(
        select([products]).where(products.c.name == name)
    ).first()
    if result is not None:
        conn.execute(
            delete(products).where(products.c.name == name)
        )
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't delete '{name}' because it's not stored in table '{table_name}'")
