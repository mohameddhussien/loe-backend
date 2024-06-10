import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class Database:
    _pool = None

    def __init__(self, host, name, user, password):
        self.host = host
        self.database = name
        self.user = user
        self.password = password
        self.connection = None

    @staticmethod
    def get_connection_pool(host, database, user, password):
        if Database._pool is None:
            Database._pool = pooling.MySQLConnectionPool(
                pool_name="my_pool",
                pool_size=5,
                pool_reset_session=True,
                host=host,
                database=database,
                user=user,
                password=password
            )
        return Database._pool

    def get_connection(self):
        return self.get_connection_pool(self.host, self.database, self.user, self.password).get_connection()

    def connect(self):
        try:
            self.connection = self.get_connection()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, params=None):
        cursor = None
        result = None
        try:
            if self.connection and self.connection.is_connected():
                cursor = self.connection.cursor(dictionary=True)
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                result = cursor.fetchall()
        except Error as e:
            print(f"Error executing query: {query}\nERROR: {e}")
        finally:
            if cursor:
                cursor.close()
        return result

    def call_stored_procedure(self, procedure_name, args=None):
        cursor = None
        result = None
        try:
            if self.connection and self.connection.is_connected():
                cursor = self.connection.cursor(dictionary=True)
                if args:
                    cursor.callproc(procedure_name, args)
                else:
                    cursor.callproc(procedure_name)
                result = []
                for res in cursor.stored_results():
                    result.extend(res.fetchall())
        except Error as e:
            print(f"Error calling stored procedure: {e}")
        finally:
            if cursor:
                cursor.close()
        return result
