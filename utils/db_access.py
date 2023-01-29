from typing import Any, List, Tuple
import psycopg
from uuid import UUID, uuid4
from utils import get_current_time_str


class Task_manager_db():
    def __init__(self) -> None:
        pass

    # Base Functions
    def connection(self) -> psycopg.connect:
        connection = psycopg.connect(
            dbname="task_manager",
            user='pi',
            password='pi',
            host='localhost',
            port='5432'
        )
        return connection

    def execute(self, query: str, values: Tuple = ()) -> None:
        conn = self.connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    def fetch(self, query: str, values: Tuple = (), fetch_one: bool = False, fetch_many: bool = False, fetch_all: bool = False) -> None:
        conn = self.connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        if fetch_one:
            fetched_data = cursor.fetchone()
        elif fetch_many:
            fetched_data = cursor.fetchmany()
        elif fetch_all:
            fetched_data = cursor.fetchall()
        else:
            raise TypeError("no fetch type was defined")
        conn.commit()
        conn.close()
        return fetched_data

    # Context.py related functions
    # TODO:
    def get_pause_status(self, task_uuid: UUID) -> bool:
        return

    def set_task_status_to_pause(self, task_uuid: UUID) -> bool:
        return

    def get_cancel_signal(self, task_uuid: UUID) -> bool:
        return

    def update_heartbeat(self, task_uuid: UUID) -> bool:
        cur_time_str = get_current_time_str()
        query = f"UPDATE tasks SET heartbeat = %s, WHERE task_uuid = %s ;"
        self.execute(query, (cur_time_str, task_uuid,))

    def update_history(self, task_uuid: UUID, most_recent_call_function_name: str) -> bool:
        return

    def check_is_task_done(self, task_uuid: UUID) -> bool:
        return

    def get_task_by_uuid(self, task_uuid) -> Any:
        query = f"SELECT * FROM tasks WHERE task_uuid = %s;"

        task_info = self.fetch(query, (task_uuid,), fetch_all=True)
        if not task_info:
            raise ValueError(
                f'failed to catch task info for task_uuid: {task_uuid}')
        return task_info

    # Initial.py related functions

    def create_tasks_table(self):
        query = "CREATE TABLE IF NOT EXISTS tasks(task_uuid uuid PRIMARY KEY, function TEXT, argument TEXT, status TEXT, start_time TEXT, expire_time TEXT,remaining_attempts int, failure_attempt_policy INT[], success_attempt_policy INT[], last_attempt_time TEXT, heartbeat TEXT, create_time TEXT, finished_time TEXT, cancel_signal bool, pause_signal bool);"
        self.execute(query)
