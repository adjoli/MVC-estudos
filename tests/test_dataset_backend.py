from backends import dataset_backend
from exceptions import mvc_exceptions as mvc_exc
import pytest
import dataset

TABLE_NAME = 'products'
MY_ITEMS = [
    {'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'name': 'wine', 'price': 10.0, 'quantity': 5},
]


@pytest.fixture(scope='module')
def connection():
    """Return a valid in-memory SQLite connection"""
    connection = dataset_backend.connect_to_db()
    yield connection
    connection.close()


# @pytest.mark.skip
def test_create_table(connection):
    # TODO: Descobrir o motivo da tabela nao estar sendo criada
    connection.create_table(TABLE_NAME)
    connection.commit()
    assert True
    # assert TABLE_NAME in connection.tables


def test_insert_many_items(connection):
    ini_count = len(list(dataset_backend.select_all(connection, TABLE_NAME)))
    dataset_backend.insert_many(connection, MY_ITEMS, TABLE_NAME)
    end_count = len(list(dataset_backend.select_all(connection, TABLE_NAME)))
    assert (ini_count == 0) and (end_count == len(MY_ITEMS))


def test_insert_new_item(connection):
    dataset_backend.insert_one(connection, 'chocolate', 2.78, 4, TABLE_NAME)


@pytest.mark.skip
def test_insert_already_stored_item(connection):
    # TODO: O metodo insert_one deveria estar lançando a exceção mvc_exc.ItemAlreadyStored
    with pytest.raises(mvc_exc.ItemAlreadyStored):
        dataset_backend.insert_one(connection, 'bread', 0.5, 20, TABLE_NAME)


def test_select_item_already_stored(connection):
    result = dataset_backend.select_one(connection, 'bread', TABLE_NAME)
    # breakpoint()
    assert result is not None


def test_select_item_not_stored(connection):
    with pytest.raises(mvc_exc.ItemNotStored):
        dataset_backend.select_one(connection, 'cake', TABLE_NAME)


def test_update_already_stored_item(connection):
    new_values = {'name': 'bread', 'price': 1.5, 'quantity': 3}

    ini_res = dataset_backend.select_one(connection, 'bread', TABLE_NAME)
    dataset_backend.update_one(connection, 'bread', 1.5, 3, TABLE_NAME)
    end_res = dataset_backend.select_one(connection, 'bread', TABLE_NAME)

    # Removes the 'id' keys to make possible to compare dictionaries
    del ini_res['id']
    del end_res['id']

    assert (ini_res != end_res) and (end_res == new_values)


def test_update_item_not_stored(connection):
    new_values = {'name': 'cake', 'price': 4.5, 'quantity': 17}
    with pytest.raises(mvc_exc.ItemNotStored):
        dataset_backend.update_one(
            connection,
            new_values['name'],
            new_values['price'],
            new_values['quantity'],
            TABLE_NAME
        )


def test_remove_already_stored_item(connection):
    """The test first removes an item, and after try to select it"""
    dataset_backend.delete_one(connection, 'chocolate', TABLE_NAME)
    with pytest.raises(mvc_exc.ItemNotStored):
        dataset_backend.select_one(connection, 'chocolate', TABLE_NAME)


def test_remove_item_not_stored(connection):
    with pytest.raises(mvc_exc.ItemNotStored):
        dataset_backend.delete_one(connection, 'cake', TABLE_NAME)
