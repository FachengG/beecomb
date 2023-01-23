from utils.db_access import Task_manager_db
from utils.context import Context
from uuid import UUID

class Bee():
    def __init__(self, task_uuid: UUID) -> None:
        self.context = Context(task_uuid)

    # TODO: scan tasks table to locate new task
    def start_work(self) -> bool:
        if self.find_new_task():
            return True
        return False
    
    def find_avaiable_task(self) -> bool:

        pass