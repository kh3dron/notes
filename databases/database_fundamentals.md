Database Fundamentals

- Relational database
  - Microsoft SQL server
  - things are linked between tables with "keys"
    - a "primary key" is a UID for a row, which can be entered as a "foreign key" to another table, defining a "relationship"
- Non-relational database
  - Not organized around tables, like relational DBs
  - "NoSQL" or not-only-sql
  - Most lack ACID transactions

- ACID transactions
  - Atomicity: each transaction is a unit. completely succeeds or fails, no partial transactions
  - Consistency: actions bring the db from legal to legal states, no creation of illegal states. prevents transactions that conflict with table rules. 
  - Isolation: concurent transactions are run as though they were run in order (double spend). Helps with concurrency control, important for scaled out DBs
  - Durability: transactions will remain committed even if system fails (non-volatile memory)

- CRUD: the four basic transactions (SQL, Rest APIs)
  - Create (INSERT, PUT)
  - Read (SELECT, GET)
  - Update (UPDATE, PUT)
  - Delete (DELETE, DELETE)

- Database Normalization
  - a series of rules for structuring a datbase - similar to principles of OOP, but for DBs
  - the normal forms: 
    - 1NF: each column of a table much hold a single value
- Database Indexing
  - improves performance of a DB, while increasing storage costs