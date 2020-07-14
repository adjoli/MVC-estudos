from backends import basic_backend
from backends import sqlite_backend
from backends import dataset_backend
from backends import sqlalchemy_orm_backend


class ModelBasic:
    def __init__(self, application_items):
        self._item_type = 'product'
        self.create_items(application_items)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_items(self, items):
        basic_backend.create_items(items)

    def create_item(self, name, price, quantity):
        basic_backend.create_item(name, price, quantity)

    def read_items(self):
        return basic_backend.read_items()

    def read_item(self, name):
        return basic_backend.read_item(name)

    def update_item(self, name, price, quantity):
        basic_backend.update_item(name, price, quantity)

    def delete_item(self, name):
        basic_backend.delete_item(name)


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


class ModelDataset:
    def __init__(self, application_items):
        self._item_type = 'product'
        self._connection = dataset_backend.connect_to_db(
            dataset_backend.DB_name)
        dataset_backend.create_table(self._connection, self._item_type)
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
        dataset_backend.insert_many(
            self.connection, items, table_name=self.item_type)

    def create_item(self, name, price, quantity):
        dataset_backend.insert_one(
            self.connection, name, price, quantity, table_name=self.item_type)

    def read_items(self):
        return dataset_backend.select_all(self.connection, table_name=self.item_type)

    def read_item(self, name):
        return dataset_backend.select_one(self.connection, name, table_name=self.item_type)

    def update_item(self, name, price, quantity):
        dataset_backend.update_one(
            self.connection, name, price, quantity, table_name=self.item_type)

    def delete_item(self, name):
        dataset_backend.delete_one(
            self.connection, name, table_name=self.item_type)


class ModelSQLAlchemyORM:
    def __init__(self, application_items):
        self._item_type = 'product'
        self._connection = sqlalchemy_orm_backend.connect_to_db()
        # self._connection = sqlalchemy_orm_backend.connect_to_db(
        #     sqlalchemy_orm_backend.DB_name)
        sqlalchemy_orm_backend.create_table()
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
        sqlalchemy_orm_backend.insert_many(
            self.connection, items, table_name=self.item_type)

    def create_item(self, name, price, quantity):
        sqlalchemy_orm_backend.insert_one(
            self.connection, name, price, quantity, table_name=self.item_type)

    def read_items(self):
        return sqlalchemy_orm_backend.select_all(self.connection, table_name=self.item_type)

    def read_item(self, name):
        return sqlalchemy_orm_backend.select_one(self.connection, name, table_name=self.item_type)

    def update_item(self, name, price, quantity):
        sqlalchemy_orm_backend.update_one(
            self.connection, name, price, quantity, table_name=self.item_type)

    def delete_item(self, name):
        sqlalchemy_orm_backend.delete_one(
            self.connection, name, table_name=self.item_type)


class ModelMongoDB:
    def __init__(self, application_items):
        pass

    @property
    def connection(self):
        pass

    @property
    def item_type(self):
        pass

    @item_type.setter
    def item_type(self, new_item_type):
        pass

    def create_items(self, items):
        pass

    def create_item(self, name, price, quantity):
        pass

    def read_items(self):
        pass

    def read_item(self, name):
        pass

    def update_item(self, name, price, quantity):
        pass

    def delete_item(self, name):
        pass
