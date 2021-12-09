from .database import session
from .models import *
from datetime import datetime
from sqlalchemy import text as text


def m2_load():
    # truncate table - no truncate in sqlite so use DELETE
    engine.execute(text('DELETE FROM m2sl').execution_options(autocommit=True))
    # load from csv
    with open('./data/M2SL.csv') as fp:
        # skip header row
        lines = fp.readlines()[1:]
        for line in lines:
            date, data = line.split(',')
            m2 = M2SL(
                date=datetime.strptime(date, '%Y-%m-%d').date(),
                m2sl = data
            )
            session.add(m2)

    session.commit()


def csv_load(tablename: str):
    # truncate table - no truncate in sqlite so use DELETE
    engine.execute(text(f'DELETE FROM {tablename.lower()}').execution_options(autocommit=True))
    # load from csv
    with open(f'./data/{tablename.upper()}.csv') as fp:
        # skip header row
        lines = fp.readlines()[1:]
        for line in lines:
            date, data = line.split(',')

            # create model class from tablename
            tbl = globals()[tablename.upper()]()
            # assign class attributes (field data)
            setattr(tbl, tbl.__table__.columns[0].name, datetime.strptime(date, '%Y-%m-%d').date())
            setattr(tbl, tbl.__table__.columns[1].name, data)
            # insert rec
            session.add(tbl)

    session.commit()


def csv_load_all():
    for table in tms_tablenames:
        print(table[0])
        csv_load(table[0])
