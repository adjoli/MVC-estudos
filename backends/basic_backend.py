import exceptions.mvc_exceptions as mvc_exc

items = list()


def create_items(app_items):
    global items
    items = app_items


def create_item(name, price, quantity):
    global items
    results = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise mvc_exc.ItemAlreadyStored(f'{name} already stored!')
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})


def read_items():
    global items
    return [item for item in items]


def read_item(name):
    global items
    myitems = list(
        filter(
            lambda x: x['name'] == name,
            items
        )
    )
    if myitems:
        return myitems[0]
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't read '{name}' because it's not stored")


def update_item(name, price, quantity):
    global items
    idx_items = list(
        filter(
            lambda i_x: i_x[1]['name'] == name,
            enumerate(items)
        )
    )
    if idx_items:
        i, item_to_update = idx_items[0][0], idx_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't update '{name}' because it's not stored")


def delete_item(name):
    global items
    idx_items = list(
        filter(
            lambda i_x: i_x[1]['name'] == name,
            enumerate(items)
        )
    )
    if idx_items:
        i, item_to_delete = idx_items[0][0], idx_items[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't delete '{name}' because it's not stored")
