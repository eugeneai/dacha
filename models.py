from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Numeric, Date, Enum
from sqlalchemy import ForeignKey
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


# class Catalog(Base, CatalogMixing):
#     """This class represents a base class for catalogs."""
#     __tablename__ = 'catalog'

#     id = Column(Integer, primary_key=True)
#     title = Column(String(50))


class Units(enum.Enum):
    cubic_meter = 1
    liter = 2
    hundred = 3
    kilowatt = 4
    # .....


class FacilityType(Base):
    __tablename__ = 'facility_type'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    unit = Column(Enum(Units))

    def __init__(self, title, unit):
        self.title = title
        self.unit = unit


class Facility(Base):
    """Объект: участок, трансорматорна будка...."""

    __tablename__ = 'facility'

    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, ForeignKey('facility_type.id'))
    title = Column(String(50))
    type = relationship("FacilityType", back_populates="facilities")


FacilityType.facilities = relationship("Facility", back_populates="type")


class Person(Base, CatalogMixing):
    """Владелец объекта"""

    __tablename__ = 'person'

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.title = value
        return value

    name = property(get_title, set_title)

    id = Column(Integer, primary_key=True)
    title = Column(String(50))

    def __init__(self, name):
        self.name = name


class Payment(Base):
    __tablename__ = 'payment'
    """Факт оплаты услуги или взнос"""
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    facility_id = Column(Integer, ForeignKey('facility.id'))
    date = Date()
    price = Numeric(11, 2)
    cost = Numeric(11, 2)

    facilities = relationship("Facility", back_populates="documents")
    persons = relationship("Person", back_populates="documents")

    def get_quantity(self):
        assert abs(float(self.price)) < 0.01, "zero price"
        return self.cost / self.price

    def set_quantity(self, value):
        self.cost = self.price * value

    quantity = property(get_quantity, set_quantity)


Facility.documents = relationship("Payment", back_populates="facilities")
Person.documents = relationship("Payment", back_populates="persons")


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
