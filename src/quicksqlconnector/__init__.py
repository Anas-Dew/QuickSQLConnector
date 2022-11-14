__version__ = '1.4.1'
from typing import Optional
import mysql.connector as mysql
from prettytable import PrettyTable


# TO MATCH SPECIFIC WORDS FROM QUERY TO PERFORM QUERY SPECIFIC TASKS
def contains_word(search_string, target_word):
    return f'{target_word}' in f'{search_string}'


class quicksqlconnector:

    def __init__(self, host: str, port: int, user: str, password: str, database=Optional[str]):

        try:  # TRYING TO CONNECT TO DB IF DB NAME PROVIDED

            self.SQL = mysql.Connect(host=f'{host}', port=port,
                                     user=f'{user}', password=f'{password}', database=f'{database}')
            # print('current database : {}'.format(database))

        except mysql.errors.ProgrammingError:  # IF DB NAME NOT FOUND CONNECT TO SERVER

            self.SQL = mysql.Connect(host=f'{host}', port=port,
                                     user=f'{user}', password=f'{password}')
            print('No database exists with name : {}'.format(database))
            print('\nConnected to MySQL Server successfully.')

        except:
            raise ValueError

    def query(self, MyQuery: str):

        table = PrettyTable()
        try:

            if contains_word(MyQuery, 'select') == True:

                sql_cursor = self.SQL.cursor()
                sql_cursor.execute(MyQuery)

                all_info = []

                for bits_of_data in sql_cursor:
                    all_info.append(bits_of_data)
                return all_info

            elif contains_word(MyQuery, 'show') == True:

                table.field_names = ['Result']
                sql_cursor = self.SQL.cursor()
                sql_cursor.execute(MyQuery)

                # all_info = []
                for bits_of_data in sql_cursor:
                    # all_info.append(bits_of_data[0])
                    table.add_row([bits_of_data[0]])
                return table

            else:

                sql_cursor = self.SQL.cursor()
                sql_cursor.execute(MyQuery)
                self.SQL.commit()

                return f'Query OK with command : {MyQuery}'

        except mysql.errors.ProgrammingError:
            print('Command Error !')
        except mysql.errors.IntegrityError:
            print('Duplicate primary key found !')
        except mysql.errors.InternalError:
            print('Unread result found')
        # except : // removed this to get more accurate, errors.
        #     print("SQL Command Error")


if __name__ == "__main__":
    DB = quicksqlconnector('localhost', 6606, 'root', 'anas9916', 'userbase')
    # print(DB.query('show databases'))
    # # print(DB.query('use usrbase'))
    # print(DB.query('show databases')[0][0])
    # print(DB.query('show tables'))
    # print(DB.query('show databases'))
    pass
