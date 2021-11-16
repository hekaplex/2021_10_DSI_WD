from .database import engine, session
from .models import M2SL
from datetime import datetime
from sqlalchemy import text as text


def m2add():

    m2 = M2SL(
        date = datetime.strptime('2014-12-04', '%Y-%m-%d').date(),
        m2sl = 125.9
    )

    session.add(m2)
    session.commit()


def m2_load():
    # truncate table - no truncate in sqlite so use DELETE
    engine.execute(text('DELETE FROM m2sl').execution_options(autocommit=True))
    # load from csv
    with open('./data/M2SL.csv') as fp:
        lines = fp.readlines()[1:]
        for line in lines:
            date, data = line.split(',')
            m2 = M2SL(
                date=datetime.strptime(date, '%Y-%m-%d').date(),
                m2sl = data
            )
            session.add(m2)

    session.commit()