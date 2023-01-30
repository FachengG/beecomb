from db_access import Db

# initial database
initial_db = Db.Task_manager_db()
initial_db.create_tasks_table()
