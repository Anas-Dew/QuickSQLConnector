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
            self.SQL.autocommit = True
        except mysql.errors.ProgrammingError:  # IF DB NAME NOT FOUND CONNECT TO SERVER

            self.SQL = mysql.Connect(host=f'{host}', port=port,
                                     user=f'{user}', password=f'{password}')
            self.SQL.autocommit = True
            print('No database exists with name : {}'.format(database))
            print('\nConnected to MySQL Server successfully.')

        except:
            raise ValueError

    def query(self, my_query: str):
        print(my_query)
        """
        It takes a query as a string, and returns the result of the query
        
        :param my_query: str
        :type my_query: str
        :return: The query is being returned.
        """

        table = PrettyTable()
        try:

            if 'select' or 'SELECT' in my_query:
                all_info = []

                with self.SQL.cursor() as cursor:
                    cursor.execute(my_query)
                    for bits_of_data in cursor:
                        all_info.append(bits_of_data)
                    cursor.close()


                return all_info

            # elif contains_word(my_query, 'show') == True:
            elif 'show' or 'SHOW' in my_query:

                table.field_names = ['Result']
                with self.SQL.cursor() as cursor:
                    cursor.execute(my_query)

                    for bits_of_data in cursor:
                        table.add_row([bits_of_data[0]])

                    cursor.close()
                return table

            else:
                with self.SQL.cursor() as cursor:
                    cursor.execute(my_query)
                    cursor.close()
                return f'Query OK with command : {my_query}'

        except Exception as e:
            print(e)


if __name__ == "__main__":
    DB = quicksqlconnector('localhost', 6606, 'root', 'anas9916', 'userbase')
    # print(DB.query('show databases'))
    # DB.query('use userbase')
    # print(DB.query('show databases')[0][0])
    # print(DB.query('show tables'))
    # print(DB.query('SELECT * FROM new_fb'))
    # DB.query('CREATE TABLE test(name varchar(10), id int(10))')
    print(DB.query("INSERT INTO test values('lex',1)"))
    # DB.query('DROP TABLE test')
    # print(DB.query('show tables'))
    print(DB.query('SELECT * FROM test'))
    pass
