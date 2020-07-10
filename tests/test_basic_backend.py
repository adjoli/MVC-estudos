import unittest
import basic_backend
import mvc_exceptions as mvc_exc

# TODO: incompleto


class TestBasicBackend(unittest.TestCase):
    def setUp(self):
        self.my_items = [
            {'name': 'bread', 'price': 0.5, 'quantity': 20},
            {'name': 'milk', 'price': 1.0, 'quantity': 10},
            {'name': 'wine', 'price': 10.0, 'quantity': 5},
        ]

    def test_item_in_list(self):
        result = basic_backend.read_item('bread')


def main():
    """Testing CRUD"""
    # TODO: migrate tests to unittest

    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    # == CREATE =====================================================
    create_items(my_items)
    create_item('beer', price=3.0, quantity=15)
    # if we try to recreate an object, we get an ItemAlreadyStored exception
    # create_item('beer', price=3.0, quantity=15)

    # == READ =======================================================
    print('READ items')
    print(read_items())
    print('READ bread')
    print(read_item('bread'))
    # if we try to read an object not stored, we get an ItemNotStored exception
    # print('READ chocolate')
    # print(read_item('chocolate'))

    # == UPDATE =====================================================
    print('UPDATE bread')
    update_item('bread', price=2.0, quantity=30)
    print(read_item('bread'))
    # if we try to update an object not stored we get an ItemNotStored exception
    # print('UPDATE chocolate')
    # print(update_item('chocolate', price=10.0, quantity=20))

    # == DELETE =====================================================
    print('DELETE beer')
    delete_item('beer')
    # if we try to delete an object not stored, we get a ItemNotStored exception
    # delete_item('beer')

    print('READ items')
    print(read_items())
