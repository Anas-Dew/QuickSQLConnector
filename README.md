## Introduction - QuickSQL
#### QuickSQL directly establishes connection between python and mysqlserver. And gives you simple interface to execute mysql commands easily.
## How to use?

* ### Use 'quicksql' keyword to import

```import quicksql```

  
* ### Creating instance of module
```DB = quicksql('host', port, 'username', 'password', 'database-name')```

  

* ### quicksql only have one method which is 'query'

> pass your 'mysql commnad' as a string in query method to execute query.


    DB.query('update people set id=90 where id=1')
    DB.query('delete from people where id=1000')
    DB.query('delete from people where id=1022')
    DB.query('insert into people value(26,4,6)')
    DB.query('select * from people')
    
## Bugs & Feedback
#### Github - [Visit Here](https://github.com/Anas-Dew/QuickSQL)


