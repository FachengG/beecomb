from typing import Any, List, Tuple
import psycopg
from uuid import UUID, uuid4
from utils.utils import get_current_time_str

class db_access():
    def __init__(self) -> None:
        self.db_access = None
        pass

    def __enter__(self):
        self.db_access = self.connection()
        return self.db_access
         
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.db_access:
            self.db_access.commit()
            self.db_access.close()
            self.db_access = None

    def connection(self) -> psycopg.connect:
        connection = psycopg.connect(
            dbname="task_manager",
            user='pi',
            password='pi',
            host='localhost',
            port='5432'
        )
        return connection

    def execute(self, query: str, values: Tuple = ()) -> None:
        conn = self.connection()
        cursor = conn.cursor()
        cursor.execute(query,values)
        conn.commit()
        conn.close()

    def fetch(self, query: str, values: Tuple = (), fetch_one:bool = False, fetch_many:bool = False, fetch_all:bool = False) -> None:
        conn = self.connection()
        cursor = conn.cursor()
        cursor.execute(query,values)
        if fetch_one:
            fetched_data = cursor.fetchone()
        elif fetch_many:
            fetched_data = cursor.fetchmany()
        elif fetch_all:
            fetched_data = cursor.fetchall()
        else:
            raise TypeError("no fetch type was defined")
        conn.commit()
        conn.close()
        return fetched_data