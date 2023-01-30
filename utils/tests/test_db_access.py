from utils.db_access import Db


def test_db_functions():
    test_db = Db(test=True)
    query = "CREATE TABLE IF NOT EXISTS tasks(task_uuid uuid PRIMARY KEY, function TEXT, argument TEXT, status TEXT, start_time TEXT,expire_time TEXT,remaining_attempts int, failure_attempt_policy INT[], success_attempt_policy INT[], last_attempt_time TEXT,heartbeat TEXT, create_time TEXT, finished_time TEXT, cancel_signal bool, pause_signal bool);"
    test_db.execute(query)
    query = "DROP TABLE tasks;"
    test_db.execute(query)
    assert 1 == 1
