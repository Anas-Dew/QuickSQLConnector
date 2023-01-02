__version__ = '1.5.3'
import mysql.connector as mysql
import sqlite3
import psycopg2

class quicksqlconnector:

    def __init__(self, database: str = None, host: str = None, port: int = None, user: str = None, password: str = None, database_name: str='quick_db'):
       
        self.database = database
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database_name = database_name

        if self.database.lower() == 'mysql':
            try:
                self.SQL = mysql.Connect(host=f'{host}', port=port,
                                         user=f'{user}', password=f'{password}')
                self.SQL.autocommit = True

            except Exception as error:
                print(error)

        elif self.database.lower() == 'sqlite3':
            try:
                self.SQL = sqlite3.connect(f'{self.database_name}.db')
            except Exception as error:
                print(error)

        elif self.database.lower() == 'postgres':
            try:
                self.SQL = psycopg2.connect(host=self.host, user=self.user, password=self.password)
                self.SQL.autocommit = True

            except Exception as error:
                print(error)

    def query(self, my_query: str, parameters=None):

        packed_query = my_query.lower()

        try:
            # with self.SQL.cursor() as cursor: # Avoiding this because SQLite doesnt work with that.
            cursor = self.SQL.cursor()
            all_info = []
            # IF YOU'VE BETTER IDEA HOW TO DEAL THIS, Open an issue: https://github.com/Anas-Dew/QuickSQLConnector/issues
            if parameters:
                cursor.execute(packed_query, parameters)
                if self.database == 'sqlite3' :
                    self.SQL.commit()
            else:
                cursor.execute(packed_query)
                if self.database == 'sqlite3' :
                    self.SQL.commit()

            for bits_of_data in cursor:
                all_info.append(bits_of_data)

            cursor.close()
            return all_info

        except Exception as e:
            print(e)


if __name__ == "__main__":
    pass
