from exceptions import mvc_exceptions as mvc_exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Numeric, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError, InvalidRequestError


DB_name = 'myDB'

# Inicializacao sera atraves de connect_to_db()
engine = None
Session = None
session = None

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True, nullable=False, unique=True)
    price = Column(Numeric(12, 2))
    quantity = Column(Integer)

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, quantity={self.quantity})"

    def to_dict(self):
        return {
            # 'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }


def connect_to_db(db=None):
    global engine
    global Session
    global session

    if db is None:
        mydb = ':memory:'
        print('New connection to in-memory SQLite DB...')
    else:
        mydb = f'{db}.db'
        print('New connection to SQLite DB...')

    engine = create_engine(f'sqlite:///{mydb}', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


# def create_table(conn, table_name):
def create_table():
    Base.metadata.create_all(engine)


def insert_one(conn, name, price, quantity, table_name):
    conn.add(
        Product(
            name=name,
            price=price,
            quantity=quantity
        )
    )
    try:
        conn.commit()
    except (InvalidRequestError, IntegrityError) as e:
        raise mvc_exc.ItemAlreadyStored(
            f'{e}: "{name}" already stored in table "{table_name}"')


def insert_many(conn, items, table_name):
    for product in items:
        conn.add(
            Product(
                name=product['name'],
                price=product['price'],
                quantity=product['quantity']
            )
        )
    conn.commit()


def select_one(conn, item_name, table_name):
    product = conn.query(Product).filter(Product.name == item_name).first()

    if product is not None:
        return product.to_dict()
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't read '{item_name}' because it's not stored in table '{table_name}'")


def select_all(conn, table_name):
    products = conn.query(Product).all()
    result = []
    for product in products:
        result.append(
            {
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity
            }
        )
    return result


def update_one(conn, name, price, quantity, table_name):
    product = conn.query(Product).filter(Product.name == name).first()

    if product is not None:
        product.price = price
        product.quantity = quantity
        conn.commit()
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't update '{name}' because it's not stored in table '{table_name}'")


def delete_one(conn, name, table_name):
    product = conn.query(Product).filter(Product.name == name).first()

    if product is not None:
        conn.delete(product)
        conn.commit()
    else:
        raise mvc_exc.ItemNotStored(
            f"Can't delete '{name}' because it's not stored in table '{table_name}'")
