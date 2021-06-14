- Table Creation
    - CREATE TABLE table_name (
            column_1 data_type,
            column_2 data_type,
        );
- Insertion
    - INSERT INTO table_name VALUES (value1, value2);
    - INSERT INTO table_name (column1, column2) VALUES (value1, value2);
- Selection
- Update
    - UPDATE table_name
        SET column1 = value1, column2=value2
    - UPDATE celebs SET twitter_handle = '@wint' WHER id=4;
- Clauses - another name for Commands, written in caps
- Alter table
    - ALTER TABLE celebs ADD COLUMN twitter_handle TEXT;
- Delete
    - DELETE FROM celebs WHERE param IS NULL;
- Constraints - configurations for columns
    - PRIMARY KEY, UNIQUE, NOT NULL, DEFAULT 'assumedvalue'

