"""
Database wire-up code.
"""
import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.settings import DATABASE_CONNECTION_URI


def get_db():
    # beings as stateless: only acquires a connection when a query is issued
    db = DbSession()
    try:
        yield db
    finally:
        db.close()


# Engine used to create connections to the actual database (proxies, in fact -- as they come from an internal pool)
# best used at module level - https://docs.sqlalchemy.org/en/13/core/connections.html
db_engine = create_engine(DATABASE_CONNECTION_URI, pool_size=5, max_overflow=0)  # default is QueuePool

# sessionmaker is a factory class for Session objects which will ask for connections from the db engine
# or release them back with close() to the connection pool (engine will keep the connection or close
# depending on the pool size/state). Session objects also implement Unit of Work pattern: tracks all db
# changes and can be used to commit/rollback transactions.
DbSession = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)  # db session later on

# Base class which will hold all metadata regarding tables, etc: used for migrations and defining models.
Base = declarative_base()

# async db wrapper using 'encode/databases' lib
async_executor = databases.Database(DATABASE_CONNECTION_URI)
