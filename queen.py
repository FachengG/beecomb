from utils.db_access import Task_manager_db
from uuid import uuid4
from bee import Bee


class Queen():
    def __init__(self, max_bee_num: int):
        self.activate_bees = []
        self.max_bee_num = max_bee_num

    def work(self):
        self.update_activate_bee_list()
        while len(self.bee_num) <= self.max_bee_num:
            self.generate_new_bee()
            self.update_activate_bee_list()

    def generate_new_bee(self) -> None:
        new_bee = Bee()
        if new_bee.start_work():
            pass
            # TODO: update job status to running
        else:
            return
            # TODO: update job status to failed_to_start
        del new_bee
        return

    def update_activate_bee_list(self) -> None:
        activate_bees = []

        for task_uuid in self.activate_bees:
            if not Task_manager_db().check_is_task_done(task_uuid):
                activate_bees.append(task_uuid)

        self.activate_bees = activate_bees
        return
