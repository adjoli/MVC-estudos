from models import ModelBasic, ModelSQLite
from views import View
from controller import Controller


my_items = [
    {'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'name': 'wine', 'price': 10.0, 'quantity': 5},
]


#c = Controller(ModelBasic(my_items), View())
c = Controller(ModelSQLite(my_items), View())

c.show_items()

# print('Deleting "wine" ...')
# c.delete_item('wine')
# c.show_items()
