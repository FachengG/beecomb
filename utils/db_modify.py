from utils.db_access import Db
from uuid import UUID
import logging
from utils.utils import get_current_time_str
from utils.query import create_signal_table_query, create_tasks_table_query

logging.basicConfig(filename="../log/db.log")


class db_modify:
    def __init__(self, database: Db = None) -> None:
        self.db = database

    def get_pause_status(self, task_uuid: UUID) -> bool:
        return

    def set_task_status_to_pause(self, task_uuid: UUID) -> bool:
        return

    def get_cancel_signal(self, task_uuid: UUID) -> bool:
        return

    def add_task(self) -> UUID:
        cur_time_str = get_current_time_str()
        tasks_table = Table("tasks")
        querry = Query.create_table("tasks").columns()

        return

    def update_heartbeat(self, task_uuid: UUID) -> bool:
        tasks_table = Table("tasks")
        cur_time_str = get_current_time_str()
        query = Query.update(tasks_table).set(tasks_table.heartbeat, cur_time_str).where(tasks_table.uuid == task_uuid)
        if not self.db.execute(query):
            logging.warning(f" task uuid: {task_uuid} failed to update heartbeat at {cur_time_str}")

    def update_history(self, task_uuid: UUID, most_recent_call_function_name: str) -> bool:
        return

    def check_is_task_done(self, task_uuid: UUID) -> bool:
        return

    def get_task_by_uuid(self, task_uuid) -> any:
        query = f"SELECT * FROM tasks WHERE task_uuid = %s;"

        task_info = self.fetch(query, (task_uuid,), fetch_all=True)
        if not task_info:
            raise ValueError(f"failed to catch task info for task_uuid: {task_uuid}")
        return task_info

    #
    # Initial.py related functions
    #
    def create_tasks_table(self):
        for query in (create_signal_table_query(), create_signal_table_query()):
            if self.db.execute(query) is False:
                logging.warning(f"db initialization with query: {query} failed")
                try:
                    exit()
                finally:
                    print(f"{self.db.database_name} db initialization failed")

        print(f"{self.db.database_name} db initialization successed")
        return
