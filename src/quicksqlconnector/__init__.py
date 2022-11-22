__version__ = '1.5'
import mysql.connector as mysql
import sqlite3
import psycopg2

class quicksqlconnector:

    def __init__(self, database: str = None, host: str = None, port: int = None, user: str = None, password: str = None, database_name=None):
        """
        It connects to a database and returns a connection object
        
        :param database: mysql, sqlite3, postgres
        :type database: str

        :param host: The hostname of the database server
        :type host: str

        :param port: The port number to connect to the database server
        :type port: int

        :param user: The username to log in as
        :type user: str

        :param password: The password of the user
        :type password: str

        :param database_name: The name of the database you want to connect to
        :type database_name: str
        """

        self.database = database
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database_name = database_name

        if self.database.lower() == 'mysql':
            try:  # TRYING TO CONNECT TO DB IF DB NAME PROVIDED

                self.SQL = mysql.Connect(host=f'{host}', port=port,
                                         user=f'{user}', password=f'{password}', database=f'{database_name}')
                self.SQL.autocommit = True

            except Exception as error:
                print(error)

        # EXPERIMENTAL AREA
        elif self.database.lower() == 'sqlite3':
            try:
                self.SQL = sqlite3.connect(f'{self.database_name}.db')
            except Exception as error:
                print(error)

        elif self.database.lower() == 'postgres':
            try:
                self.SQL = psycopg2.connect(
                    host=self.host, database=self.database_name, user=self.user, password=self.password)
                self.SQL.autocommit = True
            except Exception as error:
                print(error)

    def query(self, my_query: str, parameters=None):
        """
        It takes a query and parameters, and returns the result of the query
        
        :param my_query: The query you want to execute
        :type my_query: str

        :param parameters: A tuple of values to substitute in place of the parameters in the SQL
        statement.

        :return: A list of tuples which has data asked.
        """
        packed_query = my_query.lower()

        try:
            # with self.SQL.cursor() as cursor: # Avoiding this because SQLite doesnt work with that.
            cursor = self.SQL.cursor()
            all_info = []
            # IF YOU'VE BETTER IDEA HOW TO DEAL THIS, Open an issue: https://github.com/Anas-Dew/QuickSQLConnector/issues
            if parameters:
                cursor.execute(packed_query, parameters)
                if self.database == 'sqlite3':
                    self.SQL.commit()
            else:
                cursor.execute(packed_query)
                if self.database == 'sqlite3':
                    self.SQL.commit()

            for bits_of_data in cursor:
                all_info.append(bits_of_data)

            cursor.close()
            return all_info

        except Exception as e:
            print(e)


if __name__ == "__main__":
    # SOME TESTS WHICH I PERFORM WHILE CODING.
    # USE YOUR OWN CREDS WHEN CONTRIBUTING

    # DB = quicksqlconnector('sqlite3','localhost', 6606, 'root', 'anas9916', 'userbase')
    # DB = quicksqlconnector('mysql','localhost', 6606, 'root', 'anas9916', 'userbase')
    # DB = quicksqlconnector('postgres','localhost', 5432, 'postgres', 'anas9916', 'test')


    # MYSQL QUERY EXAMPLES
    # print(DB.query('show databases'))
    # DB.query('use userbase')
    # print(DB.query('show databases')[0][0])
    # print(DB.query('show tables'))
    # print(DB.query('SELECT * FROM new_fb '))
    # DB.query('CREATE TABLE test(name varchar(10), id int(10))')
    # print(DB.query("INSERT INTO test values(%s, %s)", ('anas', 154)))
    # DB.query('DROP TABLE test')
    # input_user = '13 or 1=1' # SQL Injection Now Prevented
    # print(DB.query("SELECT * FROM test where id= %s", (input_user,)))
    # print(DB.query("SELECT * FROM test"))

    # SQL LITE QUERY EXAMPLES
    # DB.query('DROP TABLE movie')
    # print(DB.query("CREATE TABLE movie(title varchar(1), year int(1), score int(1))"))
    # print(DB.query("""
    #     INSERT INTO movie VALUES
    #         ('Monty Python and the Holy Grail', 1975, 8.2),
    #         ('And Now for Something Completely Different', 1971, 7.5)
    # """))
    pass
