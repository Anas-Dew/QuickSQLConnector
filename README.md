[![Downloads](https://static.pepy.tech/personalized-badge/quicksqlconnector?period=month&units=international_system&left_color=black&right_color=orange&left_text=Downloads%20per%20Month)](https://pepy.tech/project/quicksqlconnector)


# 🤐 What is Quick SQL Connector ?
* #### 🖇 Saves upto 80% of code lines as compared to other libraries.
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

```DB = quicksqlconnector('host', port, 'username', 'password', 'database-name:optional')```


### quicksqlconnector only have one method which is 'query'
#### It has two arguments, query and parameters.

#### Some Examples

> pass your 'mysql commnad' as a 'string' in 'query' method to execute query.

    ```DB.query("SELECT * FROM test where id= %s", (input_user,))```
    ```DB.query("SELECT * FROM test")```
    ```DB.query('CREATE TABLE test(name varchar(10), id int(10))')```
    ```DB.query("INSERT INTO test values(%s, %s)", ('harry', 13))```

    
## 🔗Useful Links
#### PyPi - [Visit Here](https://pypi.org/project/quicksqlconnector/)
#### Website - [Visit Here](https://quicksqlconnector.web.app/)