from backends import dataset_backend


def main():
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    table_name = 'product'
    dataset_backend.create_table(dataset_backend.conn, table_name)

    dataset_backend.insert_many(
        dataset_backend.conn, items=my_items, table_name=table_name)


if __name__ == "__main__":
    main()
