from config import databaseConfig as database

import sqlalchemy as sql
from datetime import date

class Invoice(database.Base):
    __tablename__ = "invoices"

    invoiceId = sql.Column(sql.Integer, primary_key=True, index=True)
    invoiceDate = sql.Column(sql.Date, nullable=False)
    invoiceClient = sql.Column(sql.String, nullable=False)
    invoiceMount = sql.Column(sql.Float, nullable=False)
    invoiceSupplier = sql.Column(sql.String, nullable=False)
