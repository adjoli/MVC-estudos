from backends import sqlite_backend


class ModelSQLite:
    def __init__(self, application_items):
        self._item_type = 'product'
        self._connection = sqlite_backend.connect_to_db(sqlite_backend.DB_name)
        sqlite_backend.create_table(self.connection, self._item_type)
        self.create_items(application_items)

    @property
    def connection(self):
        return self._connection

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_items(self, items):
        sqlite_backend.insert_many(
            self.connection, items, table_name=self.item_type)

    def create_item(self, name, price, quantity):
        sqlite_backend.insert_one(
            self.connection, name, price, quantity, table_name=self.item_type)

    def read_items(self):
        return sqlite_backend.select_all(self.connection, table_name=self.item_type)

    def read_item(self, name):
        return sqlite_backend.select_one(self.connection, name, table_name=self.item_type)

    def update_item(self, name, price, quantity):
        sqlite_backend.update_one(
            self.connection, name, price, quantity, table_name=self._item_type)

    def delete_item(self, name):
        sqlite_backend.delete_one(
            self.connection, name, table_name=self.item_type)
