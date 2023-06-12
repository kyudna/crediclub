from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

userName = "postgres"
userPassword = "pesera11"

server = "localhost"
databaseName = "crediclub"

DATABASE_URL = "postgresql://"+userName+":"+userPassword+"@"+server+"/"+databaseName

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
