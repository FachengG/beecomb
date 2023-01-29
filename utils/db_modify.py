from db_access import db
from uuid import UUID
import logging
from utils import get_current_time_str

logging.basicConfig(filename='db.log', encoding='utf-8', level=logging.DEBUG)

def get_pause_status(self,task_uuid: UUID) -> bool:
    return

def set_task_status_to_pause(self,task_uuid: UUID) -> bool:
    return
def get_cancel_signal(self,task_uuid: UUID) -> bool:
    return

def update_heartbeat(self,task_uuid: UUID) -> bool:
    cur_time_str = get_current_time_str()
    query = f"UPDATE tasks SET heartbeat = %s, WHERE task_uuid = %s ;"
    self.execute(query,(cur_time_str,task_uuid,))
def update_history(self,task_uuid: UUID, most_recent_call_function_name: str) -> bool:
    return
def check_is_task_done(self,task_uuid: UUID) -> bool:
    return
def get_task_by_uuid(self,task_uuid) -> any:
    query = f"SELECT * FROM tasks WHERE task_uuid = %s;"
    
    task_info = self.fetch(query,(task_uuid,),fetch_all=True)
    if not task_info:
        raise ValueError(f'failed to catch task info for task_uuid: {task_uuid}')
    return task_info

# Initial.py related functions
def create_tasks_table(self):
    query = "CREATE TABLE IF NOT EXISTS tasks(task_uuid uuid PRIMARY KEY, function TEXT, argument TEXT, status TEXT, start_time TEXT,expire_time TEXT,remaining_attempts int, failure_attempt_policy INT[], success_attempt_policy INT[], last_attempt_time TEXT,heartbeat TEXT, create_time TEXT, finished_time TEXT, cancel_signal bool, pause_signal bool);"
    db().execute(query)


