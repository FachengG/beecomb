from ast import arg
from multiprocessing.sharedctypes import Value
from utils.db_access import Db
from utils.context import Context
from uuid import UUID, uuid4
from utils.utils import time_to_str
from datetime import datetime
import hashlib


class Bee:
    """
    find and execute single task
    """

    def __init__(self) -> None:
        self.uuid = None
        self.start_work()
        self.find_avaiable_task()

    def start_work(self) -> tuple(bool, UUID):
        self.uuid = self.find_avaiable_task()
        if self.uuid == None:
            return (False, None)
        return (True, self.uuid)

    def find_avaiable_task(self) -> UUID:
        return UUID


Bee.start_work()
