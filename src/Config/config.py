from environs import Env

env = Env()
env.read_env()

db_path = env.str("DB_PATH", "todo_list_app.db")

