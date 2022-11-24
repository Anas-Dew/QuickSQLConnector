![QuickSQLConnector](./src/meta%20banner.png)

Developers are struggling to execute a query and what if you need to execute another query somewhere else? That's a lot of code to rewrite again. You don't have to do this because QuickSQLConnector got you coverd!. <a href="https://quicksqlconnector.web.app/">Quick SQL Connector</a> is a python library that lets you execute MySQL, PostgreSQL, and SQLite queries with just one line of code. 

Saving 80% lines of code and get more done and it's all done in the same syntax with all SQL databases.

[![Downloads](https://static.pepy.tech/personalized-badge/quicksqlconnector?period=month&units=international_system&left_color=black&right_color=orange&left_text=Downloads%20per%20Month)](https://pepy.tech/project/quicksqlconnector)  [![PyPI version](https://badge.fury.io/py/quicksqlconnector.svg)](https://badge.fury.io/py/quicksqlconnector)  [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)  [![Generic badge](https://img.shields.io/badge/Developers-Happy-<COLOR>.svg)](https://shields.io/)



## Installation 💿

> USING PIP

    pip install quicksqlconnector

> FOR LINUX FRIENDS

    python3 pip install quicksqlconnector

To update Quick SQL Connector to the latest version, add --upgrade flag to the above commands.

## Write your first query.

### Use 'quicksqlconnector' keyword to import

    from quicksqlconnector import quicksqlconnector

### Creating instance of module

    DB = quicksqlconnector('database','host', port, 'username', 'password', 'database-name')

For database, it has 3 options (case-sensitive).
* ```mysql```
* ```sqlite3```
* ```postgres```

> quicksqlconnector only have one method which is 'query'.

    DB.query('query','parameters:optional')

> It has two arguments, query and parameters, parameters are optional.

    DB.query("SELECT * FROM test where id= %s", (input_user,))
    DB.query("SELECT * FROM test")
    DB.query('CREATE TABLE test(name varchar(10), id int(10))')
    DB.query("INSERT INTO test values(%s, %s)", ('harry', 13))


## 🔗Useful Links
* Email - [Click Here](mailto:anasraza1@yahoo.com)
* PyPi - [Visit Here](https://pypi.org/project/quicksqlconnector/)
* Website - [Visit Here](https://quicksqlconnector.web.app/)
