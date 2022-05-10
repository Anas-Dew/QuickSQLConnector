__version__ = '1.0.3'
from typing import Optional
import mysql.connector as mysql

def contains_word(search_string, target_word):
    return f'{target_word}' in f'{search_string}'

class quicksqlconnector:

    def __init__(self, host:str, port:int, user:str, password:str, database = Optional[str]):
        
        try:

            self.SQL = mysql.Connect(host=f'{host}', port=port, 
                            user=f'{user}', password=f'{password}', database=f'{database}')
            # print('current database : {}'.format(database))
        except mysql.errors.ProgrammingError :
            
            self.SQL = mysql.Connect(host=f'{host}', port=port, 
                            user=f'{user}', password=f'{password}')
            print('No database exists with name : {}'.format(database))

        except:
            raise ValueError

    def query(self, MyQuery:str):
            
        try :
            
            if contains_word(MyQuery, 'select') or contains_word(MyQuery, 'show') == True :

                sql_cursor = self.SQL.cursor()
                sql_cursor.execute(MyQuery)

                all_info = []
                for bits_of_data in sql_cursor:
                    all_info.append(bits_of_data)
                return all_info

            else :

                sql_cursor = self.SQL.cursor()
                sql_cursor.execute(MyQuery)
                self.SQL.commit()

                return f'Query OK with command : {MyQuery}'
            
        except mysql.errors.ProgrammingError:
            print('Something bad with command')
        except mysql.errors.IntegrityError:
                print('Primary Key Duplicate Error')
        except mysql.errors.InternalError:
            print('Unread result found')
        except :
            print("SQL Command Error")



if __name__ == "__main__" :
    
    DB = quicksqlconnector('localhost', 6606, 'root', 'anas9916','userbase')

    # DB.query(f"insert into fb values({22},'Anas',{22},'Delhi')")
    # print(DB.query('select * from fb where age=1'))
    print(DB.query('select * from fb'))
    # print(DB.query('use usrbase'))
    # print(DB.query('show databases'))

    # me = DB.query('select * from fb where age=1')
    # print(me)

    # print(DB.query('select * from fb where city like "%_w"'))
    # print(DB.query('desc fb'))


    pass