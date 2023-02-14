from utils.db_access import Db, TestDb
from utils.query import create_signal_table_query, create_tasks_table_query
import os

if "PYTEST_CURRENT_TEST" in os.environ:
    in_test_environment = True


# initial workflow
class Set_up:
    def __init__(self):
        self.in_test_environment = "PYTEST_CURRENT_TEST" in os.environ
        if self.in_test_environment:
            self.db = TestDb()
        else:
            self.db = Db()

    def init_db(self) -> bool:
        signal_table = self.db.execute(create_signal_table_query())
        tasks_table = self.db.execute(create_tasks_table_query())
        return True
        #  return signal_table & tasks_table
