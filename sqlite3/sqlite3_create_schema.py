import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print 'Creating schema'
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print 'Inserting initial data'

        conn.execute("""
        insert into project (name, description, deadline)
        values ('pymotw', 'Python Module of the Week', '2015-05-01')
        """)

        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about select', 'done', '2015-03-01', 'pymotw')
        """)

        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about random', 'waiting', '2015-04-01', 'pymotw')
        """)

        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about sqlite3', 'active', '2015-04-15', 'pymotw')
        """)

        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about sqlite3', 'active', '2015-04-25', 'pytmotw')
        """)

    else:
        print 'Database exists, assume schema does, too.'
