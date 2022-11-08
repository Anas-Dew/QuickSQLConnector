[![Downloads](https://pepy.tech/badge/quicksqlconnector/month)](https://pepy.tech/project/quicksqlconnector)
# 🤐 Introduction - QuickSQLConnector
* #### 🖇 Directly establishes connection between python and mysqlserver.
* #### 😃 Gives you simple interface to execute mysql commands easily.
## 💽 Pre-requisites & Installation
* #### MySQLServer and MySQL Command-Line Client should be installed on your machine.


> 😋USING PIP

* ``` pip install quicksqlconnector ```

> 😈FOR LINUX FRIENDS

* ``` python3 pip install quicksqlconnector ```

## 🙄How to use?

### Use 'quicksqlconnector' keyword to import

```  from quicksqlconnector import quicksqlconnector```

  
### Creating instance of module

```DB = quicksqlconnector('host', port, 'username', 'password', 'database-name')```


### quicksqlconnector only have one method which is 'query'



> pass your 'mysql commnad' as a 'string' in 'query' method to execute query.




    DB.query('update people set id=90 where id=1')
    DB.query('delete from people where id=1000')
    DB.query('delete from people where id=1022')
    DB.query('insert into people value(26,4,6)')
    DB.query('select * from people')
    
## 🔗Useful Links

#### PyPi - [Visit Here](https://pypi.org/project/quicksqlconnector/)
