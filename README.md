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


#### Some Examples

> pass your 'mysql commnad' as a 'string' in 'query' method to execute query.



    DB.query('update people set id=90 where id=1')
    DB.query('delete from people where id=1000')
    DB.query('delete from people where id=1022')
    DB.query('insert into people value(26,4,6)')
    DB.query('select * from people')
    
## 🔗Useful Links
#### PyPi - [Visit Here](https://pypi.org/project/quicksqlconnector/)
#### Website - [Visit Here](https://quicksqlconnector.web.app/)
