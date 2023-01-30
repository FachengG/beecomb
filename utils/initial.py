from utils.db_access import db

# initial database
initial_db = db()
initial_db.create_tasks_table()
