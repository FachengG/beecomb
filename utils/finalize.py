from utils.db_access import Db, TestDb
from utils.query import drop_tasks_table_query, drop_signal_table_query
import os


# initial workflow
class Clean_up:
    def __init__(self):
        self.in_test_environment = "PYTEST_CURRENT_TEST" in os.environ
        if self.in_test_environment:
            self.db = TestDb()
        else:
            self.db = Db()

    def purge_db(self) -> bool:
        return self.db.execute_many(drop_tasks_table_query(), drop_signal_table_query())
        #  return signal_table & tasks_table
