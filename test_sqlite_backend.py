import sqlite_backend


def main():
    """Testing CRUD"""
    # TODO: migrate tests to unittest

    table_name = 'items'
    conn = sqlite_backend.connect_to_db()  # in-memory DB
    # conn = sqlite_backend.connect_to_db(sqlite_backend.DB_name)

    sqlite_backend.create_table(conn, table_name)

    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    # == CREATE =====================================================
    sqlite_backend.insert_many(conn, my_items, table_name)
    sqlite_backend.insert_one(conn, 'beer', price=2.0,
                              quantity=5, table_name=table_name)

    # -- Duplicate insertion
    # sqlite_backend.insert_one(conn, 'milk', price=1.0,
    #                           quantity=3, table_name=table_name)

    # == READ =======================================================
    print('SELECT milk')
    print(sqlite_backend.select_one(conn, 'milk', table_name=table_name))
    print('SELECT all')
    print(sqlite_backend.select_all(conn, table_name=table_name))

    # -- Select non existing item
    #print(sqlite_backend.select_one(conn, 'pizza', table_name))

    # == UPDATE =====================================================
    print('UPDATE bread, SELECT bread')
    sqlite_backend.update_one(conn, 'bread', price=1.5,
                              quantity=5, table_name=table_name)
    print(sqlite_backend.select_one(conn, 'bread', table_name=table_name))

    # -- Update non existing item
    # sqlite_backend.update_one(conn, 'pizza', price=1.5,
    #                           quantity=5, table_name=table_name)

    # == DELETE =====================================================
    print('DELETE beer, SELECT all')
    sqlite_backend.delete_one(conn, 'beer', table_name=table_name)
    print(sqlite_backend.select_all(conn, table_name=table_name))

    # -- Delete non existing item
    # sqlite_backend.delete_one(conn, 'fish', table_name=table_name)

    conn.close()


if __name__ == "__main__":
    main()
