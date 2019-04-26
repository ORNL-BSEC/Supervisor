
# DB HPO INIT PY
# Initialize the SQLite DB for HPO
# See db-hpo-init.sql for the table schema

import os, sys

from xcorr_db import xcorr_db

def create_tables(db_hpo_init_sql):
    """ Set up the tables defined in the SQL file """
    with open(db_hpo_init_sql) as fp:
        sqlcode = fp.read()
    DB.executescript(sqlcode)
    DB.commit()

# def create_indices():
#    """ Create indices after data insertion for speed """
#     DB.execute("create index features_index on features(record_id);")
#     DB.execute("create index  studies_index on studies ( study_id);")

def get_args(argv):
    import argparse
    parser = argparse.ArgumentParser(description=
                                     'Setup the DB for CP1 HPOs.')
    parser.add_argument('db_filename',       help='The DB file name')
    args = parser.parse_args()
    return args

# Catch and print all exceptions to improve visibility of success/failure
success = False
try:
    this = os.getenv("THIS")
    args = get_args(sys.argv)
    DB = xcorr_db(args.db_filename, log=False)
    db_hpo_init_sql = this + "/db-hpo-init.sql"
    create_tables(db_hpo_init_sql)
    success = True
except Exception as e:
    import traceback
    print(traceback.format_exc())

if not success:
    print("DB: !!! INIT FAILED !!!")
    exit(1)

print("DB: initialized successfully")
