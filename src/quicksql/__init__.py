__version__ = '1.0.0'

import mysql.connector as mysql

def contains_word(search_string, target_word):
    return f'{target_word}' in f'{search_string}'

class quicksql:

    def __init__(self, host:str, port:int, user:str, password:str, database:str):

        self.SQL = mysql.Connect(host=f'{host}', port=port, 
                        user=f'{user}', password=f'{password}',
                     database=f'{database}')

    def query(self, MyQuery:str):

        try :
    
            if contains_word(MyQuery, 'select') == True :

                MyQuery = f'{MyQuery}'

                sql_cursor = self.SQL.cursor()
                sql_cursor.execute(MyQuery)

                print('Query OK')

            else :

                sql_cursor = self.SQL.cursor()
                sql_cursor.execute(MyQuery)
                self.SQL.commit()

                print('Query OK')
            
        except mysql.errors.IntegrityError:

                print('Primary Key Duplicate Error')
        except :
            
            print("SQL Command Error")




if __name__ == "__main__" :

    pass