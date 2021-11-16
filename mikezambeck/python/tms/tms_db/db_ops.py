from .database import session
from .models import M2SL
from datetime import datetime


def m2add():

    m2 = M2SL(
        date = datetime.strptime('2014-12-04', '%Y-%m-%d').date(),
        m2sl = 125.9
    )

    session.add(m2)
    session.commit()


