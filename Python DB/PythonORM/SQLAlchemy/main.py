from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql+psycopg2://postgres:test123@localhost/sql_alchemy_db'
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

Session = sessionmaker(bind=engine)
