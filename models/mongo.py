from backends import mongodb_backend


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
