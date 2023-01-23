import utils.db_access as db_access

## initial database 
initial_db = db_access.Task_manager_db()
initial_db.create_tasks_table()