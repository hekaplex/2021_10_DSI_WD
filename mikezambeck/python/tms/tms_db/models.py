from sqlalchemy import Column, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from .database import engine
# might need this stuff later...
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
# from sqlalchemy.orm import relationship


Base = declarative_base()


class M2SL(Base):
    __tablename__ = 'm2sl'
    date = Column(Date, primary_key=True, index=True)
    m2 = Column(Float)


class TVCKSSL(Base):
    __tablename__ = 'tvckssl'
    date = Column(Date, primary_key=True, index=True)
    travelers_checks = Column(Float)


class LTDACBM027NBOG(Base):
    __tablename__ = 'ltdacbm027nbog'
    date = Column(Date, primary_key=True, index=True)
    large_time_deposits = Column(Float)


class STDSL(Base):
    __tablename__ = 'stdsl'
    date = Column(Date, primary_key=True, index=True)
    small_time_deposits = Column(Float)


class RMFSL(Base):
    __tablename__ = 'rmfsl'
    date = Column(Date, primary_key=True, index=True)
    mmfs = Column(Float)


class TREASURY(Base):
    __tablename__ = 'treasury'
    date = Column(Date, primary_key=True, index=True)
    treasury_deposits = Column(Float)


Base.metadata.create_all(engine)

tms_tablenames = []
for table in Base.metadata.tables.items():
    tms_tablenames.append(table)
