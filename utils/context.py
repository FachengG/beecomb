import inspect
from time import sleep
from utils.db_access import Task_manager_db
from uuid import UUID

class Context:
    def __init__(self, task_uuid: UUID) -> None:
        self.db = Task_manager_db()
        self.task_uuid = task_uuid

    def __call__(self):
        self.check_pause_signal()
        self.check_cancel_signal()
        self.db.update_heartbeat(self.task_uuid)

        caller_func = inspect.stack()[1][3]
        self.db.update_history(self.task_uuid, caller_func)

    def check_pause_signal(self):
        pause_flag = True
        while self.db.get_pause_status(self.task_uuid):
            if pause_flag:
                self.db.set_task_status_to_pause(self.task_uuid)
                pause_flag = False
            sleep(10)

    def check_cancel_signal(self):
        if self.db.get_cancel_signal(self.task_uuid):
            self.db.set_task_status_to_canceled(self.task_uuid)
            try:
                exit()
            except:
                self.db.set_task_status_to_running(self.task_uuid)
    
    # TODO: change job status to finished
    # This function is added to the script's end.
    def end(self):
        return