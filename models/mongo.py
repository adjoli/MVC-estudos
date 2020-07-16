from backends import mongodb_backend


class ModelMongoDB:
    def __init__(self, application_items):
        self._item_type = 'items'
        self._connection = mongodb_backend.connect_to_db()
        mongodb_backend.create_table(self._item_type)
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
        mongodb_backend.insert_many(items, table_name=self.item_type)

    def create_item(self, name, price, quantity):
        mongodb_backend.insert_one(
            name, price, quantity, table_name=self.item_type)

    def read_items(self):
        return mongodb_backend.select_all()

    def read_item(self, name):
        return mongodb_backend.select_one(name, table_name=self.item_type)

    def update_item(self, name, price, quantity):
        mongodb_backend.update_one(
            name, price, quantity, table_name=self.item_type)

    def delete_item(self, name):
        mongodb_backend.delete_one(name, table_name=self.item_type)
