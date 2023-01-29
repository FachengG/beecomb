from db_access import db

# initial database
initial_db = db_access.Task_manager_db()
initial_db.create_tasks_table()
