from datetime import datetime
import uuid
import hashlib


def time_to_str(input_datetime: datetime) -> str:
    return input_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")


class Task:
    """
    create and add task details
    """

    def __init__(self) -> None:
        self.task_details = {}
        self.task_properties_updated = {}
        pass

    def label_property_not_updated(self, func):
        ready_property = set([])
        for property in self.task_details.keys():
            ready_property.add(property)

        def wrapper(*arg, **kwags):
            return func(*arg, **kwags)

        for property in self.task_details.keys():
            if self.task_properties_updated.get(property) == None:
                self.task_properties_updated[property] = False
        return wrapper(*arg, **kwags)

    def task_creation(
        self,
        function: str,
        argument: str,
        total_attempts: int = 1,
        start_time: datetime = datetime.now(),
    ) -> None:
        self.task_details["function"] = function
        self.function_md5, function_exist = self.calculate_function_md5(function)
        if not function_exist:
            raise ValueError("input function cannot be found.")
        self.task_details["status"] = "created"
        self.task_details["remaining_attempts"] = total_attempts
        self.task_details["start_time"] = start_time
        self.task_details["argument"] = argument
        self.task_details["created_time"] = time_to_str(datetime.now())
        self.task_details["uuid"] = uuid.uuid4().__str__()

    def calculate_function_md5(self, function: str) -> tuple[str, bool]:
        try:
            md5 = hashlib.md5(open(function, "rb").read()).hexdigest()
            return md5, True
        except:
            return "", False

    def add_failure_attempt_policy(self, failure_attempt_policy: list[int]) -> None:
        self.self.task_details["failure_attempt_policy"] = failure_attempt_policy
        return

    def add_success_attempt_policy(self, success_attempt_policy: list[int]) -> None:
        self.self.task_details["success_attempt_policy"] = success_attempt_policy
        return

    def add_expiration_time(self, expiration_time: datetime):
        self.self.task_details["expire_time"] = time_to_str(expiration_time)
