__version__ = '1.4.2'
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

        except mysql.errors.ProgrammingError:  # IF DB NAME NOT FOUND CONNECT TO SERVER

            self.SQL = mysql.Connect(host=f'{host}', port=port,
                                     user=f'{user}', password=f'{password}')
            print('No database exists with name : {}'.format(database))
            print('\nConnected to MySQL Server successfully.')

        except:
            raise ValueError

    def query(self, my_query: str):
        """
        It takes a query as a string, and returns the result of the query
        
        :param my_query: str
        :type my_query: str
        :return: The query is being returned.
        """

        table = PrettyTable()
        try:

            if 'select' in my_query:

                sql_cursor = self.SQL.cursor()
                sql_cursor.execute(my_query)

                all_info = []

                for bits_of_data in sql_cursor:
                    all_info.append(bits_of_data)
                return all_info

            # elif contains_word(my_query, 'show') == True:
            elif 'show' in my_query:

                table.field_names = ['Result']
                sql_cursor = self.SQL.cursor()
                sql_cursor.execute(my_query)

                for bits_of_data in sql_cursor:
                    table.add_row([bits_of_data[0]])
                return table

            else:

                sql_cursor = self.SQL.cursor()
                sql_cursor.execute(my_query)
                self.SQL.commit()
                return f'Query OK with command : {my_query}'

        except Exception as e:
            print(e)


if __name__ == "__main__":
    DB = quicksqlconnector('localhost', 6606, 'root', 'anas9916', 'userbase')
    # print(DB.query('show databases'))
    # DB.query('use usrbase')
    # print(DB.query('show databases')[0][0])
    print(DB.query('show databases'))
    # DB.query('select * from ')
    pass
