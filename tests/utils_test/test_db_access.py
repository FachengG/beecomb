from utils.db_access import TestDb
from utils.initial import Set_up
from utils.query import drop_tasks_table_and_query_table_query, create_tasks_table_query


class Test_db_functions:
    def test(self):
        set_up = Set_up()
        assert set_up.init_db() is True
        self.db = set_up.db
        assert self.db.database_name == TestDb().database_name


class Test_clean_up:
    db = TestDb()

    def test_cleanup(self):
        assert self.db.execute_many(drop_tasks_table_and_query_table_query()) == True
        create_tasks_table_query()
