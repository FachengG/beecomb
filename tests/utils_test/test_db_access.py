from utils.db_access import TestDb
from utils.initial import Set_up
from utils.query import drop_tasks_table_and_query_table_query


class Test_db_functions:
    def test(self):
        set_up = Set_up()
        assert set_up.init_db() is True


class Test_clean_up:
    db = TestDb()

    def test_cleanup(self):
        for query in drop_tasks_table_and_query_table_query():
            self.db.execute(query)
        assert 1 == 1
