import sqlite3
from sqlite3 import OperationalError, IntegrityError, ProgrammingError
import exceptions.mvc_exceptions as mvc_exc

DB_name = 'myDB'


def connect_to_db(db=None):
    if db is None:
        mydb = ':memory:'
        print('New connection to in-memory SQLite DB...')
    else:
        mydb = f'{db}.db'
        print('New connection to SQLite DB...')
    connection = sqlite3.connect(mydb)
    return connection


def disconnect_to_db(db=None, conn=None):
    if db is not DB_name:
        print('You are trying to disconnect from a wrong DB')
    if conn is not None:
        conn.close()


def connect(func):
    """Decorator to (re)open a sqlite database connection when needed.

    A database connection must be open when we want to perform a database query
    but we are in one of the following situations:
    1) there is no connection
    2) the connection is closed

    Parameters
    ----------
    func : function
        function which performs the database query

    Returns
    -------
    inner func : function
    """
    def inner_func(conn, *args, **kwargs):
        try:
            # A simple query to test if connection is open
            conn.execute(
                'SELECT name FROM sqlite_temp_master WHERE type="table"')
        except (AttributeError, ProgrammingError):
            conn = connect_to_db(DB_name)
        return func(conn, *args, **kwargs)
    return inner_func


@connect
def create_table(conn, table_name):
    table_name = scrub(table_name)
    sql = f"CREATE TABLE {table_name} (" \
        "rowid INTEGER PRIMARY KEY AUTOINCREMENT, " \
        "name TEXT UNIQUE, " \
        "price REAL, " \
        "quantity INTEGER)"
    try:
        conn.execute(sql)
    except OperationalError as e:
        print(e)


def scrub(input_string):
    """Clean a input string (to prevent SQL injection)

    Args:
        input_string (str)

    Returns:
        str: A cleaned str just with alphanumeric characters
    """
    return ''.join([k for k in input_string if k.isalnum()])


@connect
def insert_one(conn, name, price, quantity, table_name):
    table_name = scrub(table_name)
    sql = f"INSERT INTO {table_name} ('name', 'price', 'quantity') VALUES (?, ?, ?)"
    try:
        conn.execute(sql, (name, price, quantity))
        conn.commit()
    except IntegrityError as e:
        raise mvc_exc.ItemAlreadyStored(
            f'{e}: "{name}"" already stored in table "{table_name}"'
        )


@connect
def insert_many(conn, items, table_name):
    table_name = scrub(table_name)
    sql = f"INSERT INTO {table_name} ('name', 'price', 'quantity') VALUES (?, ?, ?)"
    entries = list()
    for item in items:
        entries.append((item['name'], item['price'], item['quantity']))
    try:
        conn.executemany(sql, entries)
        conn.commit()
    except IntegrityError as e:
        print(
            f"{e}: at least one in {[x['name'] for x in items]} was already stored in table '{table_name}'")


def tuple_to_dict(mytuple):
    mydict = dict()
    mydict['id'] = mytuple[0]
    mydict['name'] = mytuple[1]
    mydict['price'] = mytuple[2]
    mydict['quantity'] = mytuple[3]
    return mydict


@connect
def select_one(conn, item_name, table_name):
    table_name = scrub(table_name)
    item_name = scrub(item_name)
    sql = f'SELECT * FROM {table_name} WHERE name="{item_name}"'
    c = conn.execute(sql)
    result = c.fetchone()
    if result is not None:
        return tuple_to_dict(result)
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't read '{item_name}' because it's not stored in table '{table_name}'")


@connect
def select_all(conn, table_name):
    table_name = scrub(table_name)
    sql = f'SELECT * FROM {table_name}'
    c = conn.execute(sql)
    results = c.fetchall()
    return list(map(lambda x: tuple_to_dict(x), results))


@connect
def update_one(conn, name, price, quantity, table_name):
    table_name = scrub(table_name)
    sql_check = f'SELECT EXISTS(SELECT 1 FROM {table_name} WHERE name=? LIMIT 1)'
    sql_update = f'UPDATE {table_name} SET price=?, quantity=? WHERE name=?'
    c = conn.execute(sql_check, (name, ))
    result = c.fetchone()
    if result[0]:
        c.execute(sql_update, (price, quantity, name))
        conn.commit()
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't update '{name}' because it's not stored in table '{table_name}'")


@connect
def delete_one(conn, name, table_name):
    table_name = scrub(table_name)
    sql_check = f'SELECT EXISTS(SELECT 1 FROM {table_name} WHERE name=? LIMIT 1)'
    sql_delete = f'DELETE FROM {table_name} WHERE name=?'
    c = conn.execute(sql_check, (name, ))
    result = c.fetchone()
    if result[0]:
        c.execute(sql_delete, (name, ))
        conn.commit()
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't delete '{name}' because it's not stored in table '{table_name}''")
