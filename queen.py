from hashlib import new
from time import sleep
from typing import NoReturn
from utils.db_access import Db
from uuid import uuid4
from bee import Bee


class Queen():
    def __init__(self, max_bee_num: int, test_env: bool = False, bee_wait_for_job_time_constant: float = 1, queen_remove_finished_bee_time_constant: float = 1) -> None:
        self.test_env = test_env
        self.bee_wait_for_job_time_constant = bee_wait_for_job_time_constant
        self.queen_remove_finished_bee_time_constant = queen_remove_finished_bee_time_constant
        self.queen_uuid = uuid4()
        self.activate_bees_set = set()
        self.max_activate_bees = max_bee_num

    def work(self) -> NoReturn:
        self.update_activate_bee_list()
        while True:
            while len(self.activate_bees_set) <= self.max_activate_bees:
                self.generate_new_bee()
            while self.remove_finished_bee() == 0:
                sleep(self.queen_remove_finished_bee_time_constant)
            Db(self.test_env).(self.queen_uuid, "running")

    def generate_new_bee(self) -> None:
        bee_uuid = uuid4()
        new_bee = Bee(bee_uuid)
        while new_bee.start_work() != True:
            sleep(self.bee_wait_for_job_time_constant)
        self.activate_bees_set.add(bee_uuid)
        del new_bee
        return

    def remove_finished_bee(self):
        removed_bee_count = 0
        for activate_bee_uuid in self.activate_bees_set:
            if Db(self.test_env).get_task_status(activate_bee_uuid) in ('Finished'):
                self.activate_bees_set.remove(activate_bee_uuid)
                removed_bee_count += 1
        return removed_bee_count
