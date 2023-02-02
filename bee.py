from utils.db_access import Db
from utils.context import Context
from uuid import UUID, uuid4

class Bee():
    def __init__(self, task_uuid: UUID) -> None:
        self.context = Context(task_uuid)

    # TODO: scan tasks table to locate new task
    def start_work(self) -> bool:
        if self.find_avaiable_task():
            return True
        return False

    def find_avaiable_task(self) -> UUID:
        
        return UUID
        pass

