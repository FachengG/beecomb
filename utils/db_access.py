from typing import Tuple
import psycopg
import logging


logging.basicConfig(filename='../log/db.log')


class Db():
    def __init__(self) -> None:
        self.db_connection = None
        pass

    def __enter__(self) -> psycopg.connect:
        self.db_connection = self.connection()
        return self.db_connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.db_connection:
            self.db_connection.commit()
            self.db_connection.close()
            self.db_connection = None

    def connection(self) -> psycopg.connect:
        connection = psycopg.connect(dbname="task_manager",
                                     user='pi',
                                     password='pi',
                                     host='localhost',
                                     port='5432')
        return connection

    def execute(self, query: str, values: Tuple = ()) -> bool:
        conn = self.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, values)
        except:
            logging.warning(
                f"db execute query: '{query}' with values: '{values}' failed")
            return False
        finally:
            conn.commit()
            conn.close()
        return True

    def fetch(self, query: str, values: Tuple = (), fetch_one: bool = False, fetch_many: bool = False, fetch_all: bool = False) -> Tuple(bool, any):
        conn = self.connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        if fetch_one:
            try:
                fetched_data = cursor.fetchone()
            except:
                logging.warning(
                    f"db fetch one query: '{query}' with values: '{values}' failed")
                return (False, None)
            finally:
                conn.commit()
                conn.close()

        elif fetch_many:
            try:
                fetched_data = cursor.fetchmany()
            except:
                logging.warning(
                    f"db fetch many query: '{query}' with values: '{values}' failed")
                return (False, None)
            finally:
                conn.commit()
                conn.close()

        elif fetch_all:
            try:
                fetched_data = cursor.fetchall()
            except:
                logging.warning(
                    f"db fetch all query: '{query}' with values: '{values}' failed")
                return (False, None)
            finally:
                conn.commit()
                conn.close()

        else:
            raise TypeError("no fetch type was defined")

        return (True, fetched_data)


class CoefficientTurningDb(Db):
    def __init__(self):
        super().__init__(self)

    def connection(self) -> psycopg.connect:
        connection = psycopg.connect(dbname="coefficient_turning",
                                     user='pi',
                                     password='pi',
                                     host='localhost',
                                     port='5432')
        return connection


#
# Test Section
#

class TestDb(Db):
    def __init__(self):
        super().__init__(self)

    def connection(self) -> psycopg.connect:
        connection = psycopg.connect(dbname="test_task_manager",
                                     user='pi',
                                     password='pi',
                                     host='localhost',
                                     port='5432')
        return connection


class TestCoefficientTurningDb(Db):
    def __init__(self):
        super().__init__(self)

    def connection(self) -> psycopg.connect:
        connection = psycopg.connect(dbname="test_coefficient_turning",
                                     user='pi',
                                     password='pi',
                                     host='localhost',
                                     port='5432')
        return connection
