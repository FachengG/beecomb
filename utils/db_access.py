import psycopg
import logging


logging.basicConfig(filename="../log/db.log")


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
            dbname="master", user="pi", password="pi", host="localhost", port="5432"
        )
        return connection

    def execute(self, query: str, values: tuple = tuple()) -> bool:
        conn = self.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, values)
        except:
            logging.warning(
                f"{self.database_name} execute query: '{query}' with values: '{values}' failed"
            )
            return False
        finally:
            conn.commit()
            conn.close()
        return True

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
                logging.warning(
                    f"{self.database_name} fetch one query: '{query}' with values: '{values}' failed"
                )
                return (False, None)
            finally:
                conn.commit()
                conn.close()

        elif fetch_many:
            try:
                fetched_data = cursor.fetchmany()
            except:
                logging.warning(
                    f"{self.database_name} fetch many query: '{query}' with values: '{values}' failed"
                )
                return (False, None)
            finally:
                conn.commit()
                conn.close()

        elif fetch_all:
            try:
                fetched_data = cursor.fetchall()
            except:
                logging.warning(
                    f"{self.database_name} fetch all query: '{query}' with values: '{values}' failed"
                )
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
    __test__ = False

    def __init__(self):
        self.database_name = "TestDb"

    def connection(self) -> psycopg.connect:
        connection = psycopg.connect(
            dbname="test", user="pi", password="pi", host="localhost", port="5432"
        )
        return connection
