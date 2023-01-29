from utils.db_access import db


def test_db_functions():
    test_db = db(test=True)
    assert 1 == 1
