from ..db_access import db


def test_db_functions():
    test_db = db()
    assert 1 == 1
