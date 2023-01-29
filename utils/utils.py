from datetime import datetime


def get_current_time_str() -> str:
    current_datetime = datetime.now()
    current_date_time = current_datetime.strftime("%m%d%Y%H%M%S")
    return current_date_time
