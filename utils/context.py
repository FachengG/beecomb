import inspect
from time import sleep
from utils.db_access import Db
from uuid import UUID


class Context:
    def __init__(self, task_uuid: UUID) -> None:
        self.db = Db()
        self.task_uuid = task_uuid

    def __call__(self):
        self.check_pause_signal()
        self.check_cancel_signal()
        self.db.update_heartbeat(self.task_uuid)

        caller_func = inspect.stack()[1][3]
        self.db.update_history(self.task_uuid, caller_func)

    def check_pause_signal(self):
        pause_flag = True
        while self.db.check_pause_status(self.task_uuid) in ("pausing", "paused"):
            if pause_flag:
                self.db.set_task_status(self.task_uuid, "paused")
                pause_flag = False
            sleep(5)
        self.db.set_task_status(self.task_uuid, "resumed")

    def check_cancel_signal(self):
        most_recent_status = self.db.get_task_status(self.task_uuid)
        if self.db.check_cancel_status(self.task_uuid):
            self.db.set_task_status(self.task_uuid, "canceled")
            try:
                exit()
            except:
                self.db.set_task_status(self.task_uuid, most_recent_status)

    def task_finished(self):
        self.db.set_task_status(self.task_uuid, "finished")
        return

    # DB: check_cancel_status, set_task_status, check_pause_status, get_task_status, update_heartbeat, update_history
