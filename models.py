from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Decimal, Date
import enum

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


class Person(Base):
    """Владелец объекта"""


class PaymentDocument(Base):
    """Оплата услуги или взнос"""
    date = Date()
    amount = Decimal(11, 2)


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
