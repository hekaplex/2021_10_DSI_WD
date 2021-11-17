from tms_db import db_ops


if __name__ == '__main__':

    db_ops.csv_load_all()
    db_ops.csv_load('m2sl')
    # db_ops.m2add()
    print('fin')
