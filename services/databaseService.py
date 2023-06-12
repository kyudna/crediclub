from config import databaseConfig as database

def addTables():
        return database.Base.metadata.create_all(bind=database.engine)

def getDB():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

