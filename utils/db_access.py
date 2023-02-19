import psycopg
import logging
import os
import utils.utils as utils

logging.basicConfig(filename=utils.utils_abs_log_path_generator("db.log"))


class Db:
    def __init__(self) -> None:
        self.database_name = "Db"
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
        connection = psycopg.connect(
            dbname="master",
            user="pi",
            password="pi",
            host="localhost",
            port="5432",
        )
        return connection

    def execute(self, query: str, values: tuple = tuple()) -> bool:
        conn = self.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, values)
        except:
            logging.warning(f"{self.database_name} execute query: '{query}' with values: '{values}' failed")
            return False
        finally:
            conn.commit()
            conn.close()
        return True

    def execute_many(self, *arg: str | tuple) -> bool:
        execute_result = True
        for query_and_values in arg:
            if type(query_and_values) is str:
                execute_result = self.execute(query_and_values) and execute_result
            elif type(query_and_values) is tuple:
                execute_result = self.execute(query_and_values[0], query_and_values[1]) and execute_result
            if execute_result == False:
                return execute_result
        return execute_result

    def fetch(
        self,
        query: str,
        values: tuple = tuple(),
        fetch_one: bool = False,
        fetch_many: bool = False,
        fetch_all: bool = False,
    ) -> tuple([bool, any]):
        conn = self.connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        if fetch_one:
            try:
                fetched_data = cursor.fetchone()
            except:
                logging.warning(f"{self.database_name} fetch one query: '{query}' with values: '{values}' failed")
                return (False, None)
            finally:
                conn.commit()
                conn.close()

        elif fetch_many:
            try:
                fetched_data = cursor.fetchmany()
            except:
                logging.warning(f"{self.database_name} fetch many query: '{query}' with values: '{values}' failed")
                return (False, None)
            finally:
                conn.commit()
                conn.close()

        elif fetch_all:
            try:
                fetched_data = cursor.fetchall()
            except:
                logging.warning(f"{self.database_name} fetch all query: '{query}' with values: '{values}' failed")
                return (False, None)
            finally:
                conn.commit()
                conn.close()

        else:
            raise TypeError("no fetch type was defined")

        return (True, fetched_data)


#
# Test Section
#


class TestDb(Db):
    __test__ = True

    def __init__(self):
        self.database_name = "TestDb"

    def connection(self) -> psycopg.connect:
        connection = psycopg.connect(
            dbname="test",
            user="pi",
            password="pi",
            host="localhost",
            port="5432",
        )
        return connection
