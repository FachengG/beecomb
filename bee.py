from utils.db_access import Db
from utils.context import Context
from uuid import UUID, uuid4

class Bee():
    def __init__(self,) -> None:
        self.uuid = None

    def start_work(self) -> tuple(bool,UUID):
        self.uuid = self.find_avaiable_task()
        if self.uuid == None:
            return (False,None)
        return (True,self.uuid)

    def find_avaiable_task(self) -> UUID:
        
        return UUID
