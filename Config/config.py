from environs import Env

env = Env()
env.read_env()

# Databasepad
db_path = env.str("DB_PATH", "data/todo.db")
