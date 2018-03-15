from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Numeric, Date, Enum
import enum

SESSION = None
ENGINE = None

BASE = declarative_base()

Base = BASE


class CatalogMixing(object):
    def __repr__(self):
        return "<{}(id='{}', title='{}')>".format(self.__class__,
                                                  self.id,
                                                  self.title)


class Catalog(Base, CatalogMixing):
    """This class represents a base class for catalogs."""
    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))


class AmountDocument(Base):
    __tablename__ = 'amount'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)

    def __init__(self, amount=0, records=[]):
        self.amount = amount
        self.records = records


class Units(enum.Enum):
    litr = 1
    qube = 2
    # .....


class ServiceType(Base):
    __tablename__ = 'service_type'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    unit = Column(Enum(Units))


class Service(Base):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    type = relationship("ServiceType", back_populates="services")


class FacilityType():
    __tablename__ = 'facility_type'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    unit = Column(Enum(Units))


class Facility(Base):
    """Объект: участок, трансорматорна будка...."""

    __tablename__ = 'facility'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    type = relationship("FacilityType", back_populates="facilities")


class Person(Base, CatalogMixing):
    """Владелец объекта"""

    __tablename__ = 'person'

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.name = value
        return value

    name = property(get_title, set_title)

    id = Column(Integer, primary_key=True)
    title = Column(String(50))


class PaymentDocument(Base):
    __tablename__ = 'payment_document'
    """Оплата услуги или взнос"""
    id = Column(Integer, primary_key=True)
    date = Date()
    amount = Numeric(11, 2)


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
