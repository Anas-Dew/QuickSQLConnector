from __init__ import quicksqlconnector

if __name__ == "__main__":
    # SOME TESTS WHICH I PERFORM WHILE CODING.
    # USE YOUR OWN CREDS WHEN CONTRIBUTING

    # DB = quicksqlconnector('mysql','localhost', 6606, 'root', 'anas9916')

    # # MYSQL QUERY EXAMPLES
    # DB.query('CREATE DATABASE test_database;')
    # print(DB.query('show databases'))
    # DB.query('use userbase')
    # print(DB.query('show databases')[0][0])
    # print(DB.query('show tables'))
    # print(DB.query('SELECT * FROM new_fb '))
    # DB.query('CREATE TABLE test(name varchar(10), id int(10))')
    # print(DB.query("INSERT INTO test values(%s, %s)", ('anas', 154)))
    # # DB.query('DROP TABLE test')
    # input_user = '13 or 1=1' # SQL Injection Now Prevented
    # print(DB.query("SELECT * FROM test where id= %s", (input_user,)))
    # print(DB.query("SELECT * FROM test"))

    # # SQL LITE QUERY EXAMPLES
    # DB = quicksqlconnector('sqlite3', database_name='hello')
    # DB.query('DROP TABLE movie')
    # print(DB.query("CREATE TABLE movie(title varchar(1), year int(1), score int(1))"))
    # print(DB.query("""
    #     INSERT INTO movie VALUES
    #         ('Monty Python and the Holy Grail', 1975, 8.2),
    #         ('And Now for Something Completely Different', 1971, 7.5)
    # """))

    # POSTGRESQL EXAMPLES
    # DB = quicksqlconnector('postgres','localhost', 5432, 'postgres', 'anas9916')
    # print(DB.query('SELECT datname FROM pg_database'))

    pass
