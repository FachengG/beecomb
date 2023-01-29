import sys
sys.path.append('../')
from db_access  import Task_manager_db
import psycopg

def test_task_manager_db():
    assert 1 == 1