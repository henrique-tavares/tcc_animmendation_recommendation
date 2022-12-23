from psycopg_pool import ConnectionPool
from entities.env import Env

pg_pool = ConnectionPool(Env.db_url)
