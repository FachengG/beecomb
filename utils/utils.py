from datetime import datetime

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
