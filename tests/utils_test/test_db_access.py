from utils.db_access import TestDb
from utils.initial import Set_up
from utils.query import drop_all_tables


class Test_db_functions:
    def test(self):
        set_up = Set_up()
        assert set_up.init_db() is True


class Test_clean_up:
    db = TestDb()

    def cleanup(db):
        for query in drop_all_tables():
            db.execute(query)
