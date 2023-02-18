from datetime import datetime
import uuid
import hashlib
import os


def time_to_str(input_datetime: datetime) -> str:
    return input_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")


def utils_abs_log_path_generator(log_file_name: str) -> str:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir_list = list(root_dir.split("/"))
    if root_dir_list[-1] != "utils":
        raise TypeError("the function is only for utils dir")
    root_dir_list = root_dir_list[1:-1] + ["log"] + [log_file_name]
    return "/" + "/".join(root_dir_list)


class Task:
    """
    create and add task details
    """

    def __init__(self) -> None:
        self.task_details = {}
        self.task_properties_need_to_update = {}
        pass

    def label_property_need_to_update(func):
        def magic(self):
            ready_property = set([])
            for property in self.task_details.keys():
                ready_property.add(property)

            def wrapper(*arg, **kwargs):
                return func(*arg, **kwargs)

            for property in self.task_details.keys():
                if property in ready_property:
                    continue
                else:
                    self.task_properties_need_to_update[property] = True

            return wrapper

        return magic

    @label_property_need_to_update
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

    @label_property_need_to_update
    def add_failure_attempt_policy(self, failure_attempt_policy: list[int]) -> None:
        self.self.task_details["failure_attempt_policy"] = failure_attempt_policy
        return

    @label_property_need_to_update
    def add_success_attempt_policy(self, success_attempt_policy: list[int]) -> None:
        self.self.task_details["success_attempt_policy"] = success_attempt_policy
        return

    @label_property_need_to_update
    def add_expiration_time(self, expiration_time: datetime):
        self.self.task_details["expire_time"] = time_to_str(expiration_time)
