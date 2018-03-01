from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

SESSION = None
ENGINE = None

BASE = declarative_base()

Base = BASE


class Catalog(Base):
    """This class represents a base class for catalogs."""
    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))

    def __repr__(self):
        return "<{}(id='{}', title='{}')>".format(self.__class__,
                                                  self.id,
                                                  self.title)


class AmountDocument(Base):
    __tablename__ = 'amount'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)

    def __init__(self, amount=0, records=[]):
        self.amount = amount
        self.records = records


def create_session(engine):
    from sqlalchemy.orm import sessionmaker
    global SESSION
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    SESSION = Session()
    return SESSION


def create_debug_engine(echo=False):
    from sqlalchemy import create_engine

    global ENGINE, BASE
    ENGINE = create_engine('sqlite:///:memory:', echo=echo)
    BASE.metadata.create_all(ENGINE)
    return ENGINE


def create_release_engine(echo=False):
    raise RuntimeError("Not implemented!")
    return ENGINE


def print_session():
    global SESSION
    print(SESSION)
