from models import ModelBasic, ModelSQLite, ModelDataset, ModelSQLAlchemyORM
from views import View
from controller import Controller


my_items = [
    {'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'name': 'wine', 'price': 10.0, 'quantity': 5},
]


# c = Controller(ModelBasic(my_items), View())
# c = Controller(ModelSQLite(my_items), View())
# c = Controller(ModelDataset(my_items), View())
c = Controller(ModelSQLAlchemyORM(my_items), View())

c.show_items()

c.insert_item('chocolate', 2.78, 4)

# ITEM REPETIDO
# c.insert_item('milk', 2.78, 4)

c.update_item('milk', 1.23, 4)

# c.show_item('milks')
c.delete_item('wine')


c.show_items(bullet_points=True)
