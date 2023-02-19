from uuid import UUID, uuid4
from pypika import Query, Table, Column, terms, queries
from utils.task import Task


#
# Decorator
#
def query_to_string(func) -> list[str] | str:
    def wrapper(*args, **kwargs):
        if type(func(*args, **kwargs)) is list:
            return [str(q) + ";" for q in func(*args, **kwargs)]
        return str(func(*args, **kwargs)) + ";"

    return wrapper


#
# Queries
#
@query_to_string
def create_tasks_table_query() -> queries.CreateQueryBuilder:
    tasks_table_query = (
        Query.create_table("tasks")
        .columns(
            Column("task_uuid", "TEXT", nullable=False),
            Column("function", "TEXT", nullable=False),
            Column("argument", "TEXT"),
            Column("status", "TEXT", nullable=False),
            Column("start_time", "TEXT"),
            Column("expire_time", "TEXT"),
            Column("remaining_attempts", "INT", nullable=False),
            Column("failure_attempt_policy", "INT[]"),
            Column("success_attempt_policy", "INT[]"),
            Column("last_attempt_time", "TEXT"),
            Column("heartbeat", "TEXT"),
            Column("created_time", "TEXT", nullable=False),
            Column("finished_time", "TEXT"),
            Column("function_md5", "UUID NOT NULL", nullable=False),
            Column("ready", "BOOL", nullable=False, default=False),
        )
        .unique("task_uuid")
        .primary_key("task_uuid")
    )
    return tasks_table_query


@query_to_string
def create_signal_table_query() -> queries.CreateQueryBuilder:
    signal_table_query = (
        Query.create_table("signal")
        .columns(
            Column("task_uuid", "UUID", nullable=False),
            Column("cancel_signal", "bool"),
            Column("pause_signal", "bool"),
        )
        .unique("task_uuid")
        .primary_key("task_uuid")
    )
    return signal_table_query


@query_to_string
def drop_tasks_table_query() -> queries.CreateQueryBuilder:
    return Query.drop_table("tasks")


@query_to_string
def drop_signal_table_query() -> queries.CreateQueryBuilder:
    return Query.drop_table("signal")


@query_to_string
def create_new_task(task: Task) -> UUID:
    tasks_table = Table("tasks")
    tasks_table_query = Query.into(tasks_table)

    return tasks_table_query
