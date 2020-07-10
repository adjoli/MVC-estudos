class View:
    @staticmethod
    def show_bullet_point_list(item_type, items):
        print(f'--- {item_type.upper()} LIST ---')
        for item in items:
            print(f'* {item}')

    @staticmethod
    def show_number_point_list(item_type, items):
        print(f'--- {item_type.upper()} LIST ---')
        for i, item in enumerate(items):
            print(f'{i+1}. {item}')

    @staticmethod
    def show_item(item_type, item, item_info):
        print('//////////////////////////////////////////////////////')
        print(f'Goog news, we have some {item.upper()}!')
        print(f'{item_type.upper()} INFO: {item_info}')
        print('//////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item, err):
        print('||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        print(f"We are sorry, we have no {item.upper()}!")
        print(f'{err.args[0]}')
        print('||||||||||||||||||||||||||||||||||||||||||||||||||||||')

    @staticmethod
    def display_item_already_stored_error(item, item_type, err):
        print('******************************************************')
        print(
            f"Hey! we already have {item.upper()} in your {item_type.upper()} list!")
        print(f'{err.args[0]}')
        print('******************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item, item_type, err):
        print('******************************************************')
        print(
            f"We don't have any {item.upper()} in your {item_type.upper()} list! Please insert it first!")
        print(f'{err.args[0]}')
        print('******************************************************')

    @staticmethod
    def display_item_stored(item, item_type):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(
            f"Hooray! We have just added some {item.upper()} to our {item_type.upper()} list!")
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_item_type(older, newer):
        print('--- --- --- --- --- --- --- --- --- --- --- --- --- --')
        print(f"Change item type from {older} to {newer}")
        print('--- --- --- --- --- --- --- --- --- --- --- --- --- --')

    @staticmethod
    def display_item_updated(item, o_price, o_quantity, n_price, n_quantity):
        print('======================================================')
        print(f"Change {item} price: {o_price} --> {n_price}")
        print(f"Change {item} quantity: {o_quantity} --> {n_quantity}")
        print('======================================================')

    @staticmethod
    def display_item_deletion(name):
        print('------------------------------------------------------')
        print(f"We have just removed '{name}' from our list!")
        print('------------------------------------------------------')
