__version__ = '1.4.4'
from typing import Optional
import mysql.connector as mysql
from prettytable import PrettyTable


class quicksqlconnector:

    def __init__(self, host: str, port: int, user: str, password: str, database=Optional[str]):
        """
        It tries to connect to a database, if it fails it tries to connect to the server
        
        :param host: The hostname of the MySQL server
        :type host: str
        :param port: The port number to use when connecting to the MySQL server
        :type port: int
        :param user: The username to log in as
        :type user: str
        :param password: str, database=Optional[str]
        :type password: str
        :param database: Optional[str]
        """

        try:  # TRYING TO CONNECT TO DB IF DB NAME PROVIDED

            self.SQL = mysql.Connect(host=f'{host}', port=port,
                                     user=f'{user}', password=f'{password}', database=f'{database}')
            self.SQL.autocommit = True
        except mysql.errors.ProgrammingError:  # IF DB NAME NOT FOUND CONNECT TO SERVER

            self.SQL = mysql.Connect(host=f'{host}', port=port,
                                     user=f'{user}', password=f'{password}')
            self.SQL.autocommit = True
            print('No database exists with name : {}'.format(database))
            print('\nConnected to MySQL Server successfully.')

        except:
            raise ValueError

    def query(self, my_query: str, parameters=None):
        packed_query = my_query.lower()
        table = PrettyTable()

        try:

            if 'select' in packed_query:

                all_info = []
                with self.SQL.cursor() as cursor:
                    # IF YOU'VE BETTER IDEA HOW TO DEAL THIS, Open an issue: https://github.com/Anas-Dew/QuickSQLConnector/issues
                    if parameters:
                        cursor.execute(packed_query, parameters)
                    else:
                        cursor.execute(packed_query)

                    for bits_of_data in cursor:
                        all_info.append(bits_of_data)
                    cursor.close()

                return all_info

            elif 'show' in packed_query:
                
                table.field_names = ['Result']
                with self.SQL.cursor() as cursor:
                    # IF YOU'VE BETTER IDEA HOW TO DEAL THIS, Open an issue: https://github.com/Anas-Dew/QuickSQLConnector/issues
                    if parameters:
                        cursor.execute(packed_query, parameters)
                    else:
                        cursor.execute(packed_query)

                    for bits_of_data in cursor:
                        table.add_row([bits_of_data[0]])

                    cursor.close()
                return table

            else:
                with self.SQL.cursor() as cursor:
                    # IF YOU'VE BETTER IDEA HOW TO DEAL THIS, Open an issue: https://github.com/Anas-Dew/QuickSQLConnector/issues
                    if parameters:
                        cursor.execute(packed_query, parameters)
                    else:
                        cursor.execute(packed_query)
                    cursor.close()
                return f'Query OK with command : {packed_query}'

        except Exception as e:
            print(e)


if __name__ == "__main__":
    # SOME TESTS WHICH I PERFORM WHILE CODING.
    # USE YOUR OWN CREDS WHEN CONTRIBUTING

    DB = quicksqlconnector('localhost', 6606, 'root', 'anas9916', 'userbase')
    # print(DB.query('show databases'))
    # DB.query('use userbase')
    # print(DB.query('show databases')[0][0])
    # print(DB.query('show tables'))
    # print(DB.query('SELECT * FROM new_fb '))
    # DB.query('CREATE TABLE test(name varchar(10), id int(10))')
    # print(DB.query("INSERT INTO test values(%s, %s)", ('harry', 13)))
    # DB.query('DROP TABLE test')
    # print(DB.query('show tables'))
    # input_user = '12 or 1=1' # SQL Injection Now Prevented
    # print(DB.query("SELECT * FROM test where id= %s", (input_user,)))
    # print(DB.query("SELECT * FROM test"))
    pass
