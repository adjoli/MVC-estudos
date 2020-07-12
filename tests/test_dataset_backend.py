from backends import dataset_backend


def main():
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    table_name = 'product'

    conn = dataset_backend.connect_to_db(dataset_backend.DB_name)

    dataset_backend.create_table(conn, table_name)
    print(dataset_backend.select_all(conn, table_name=table_name))

    dataset_backend.insert_many(conn, items=my_items, table_name=table_name)

    # print('INSERT chcolate')
    # dataset_backend.insert_one(
    #     conn, 'chocolate', 2.3, 7, table_name=table_name)

    dataset_backend.insert_many(conn,
                                [
                                    {'name': 'water', 'price': 4.1, 'quantity': 3},
                                    {'name': 'rice', 'price': 6.7, 'quantity': 8},
                                    {'name': 'maionese',
                                        'price': 5.78, 'quantity': 5},
                                ],
                                table_name=table_name
                                )

    dataset_backend.update_one(conn, 'wine', 2.87, 1, table_name=table_name)

    # dataset_backend.delete_one(conn, 'milk', table_name=table_name)

    for i in dataset_backend.select_all(conn, table_name=table_name):
        print(i)


if __name__ == "__main__":
    main()
