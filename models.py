from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

SESSION = None
ENGINE = None

BASE = declarative_base()


class Record(BASE):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<{}(id='{}')>".format(self.__class__, self.id)


class Catalog(Record):
    """This class represents a base class for catalogs."""
    __tablename__ = 'catalog'

    title = Column(String(50))

    def __repr__(self):
        return "<{}(id='{}', title='{}')>".format(self.__class__,
                                                  self.id,
                                                  self.title)


class Document(Record):
    """A Document"""
    __tablename__ = 'document'


class AmountDocument(Document):
    __tablename__ = 'amount'
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
    global ENGINE
    ENGINE = create_engine('sqlite:///:memory:', echo=echo)
    return ENGINE


def create_release_engine(echo=False):
    raise RuntimeError("Not implemented!")
    return ENGINE
