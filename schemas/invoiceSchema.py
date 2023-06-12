from pydantic import BaseModel
from datetime import date

class BaseInvoice(BaseModel):
    invoiceDate: date
    invoiceClient: str
    invoiceMount: float
    invoiceSupplier: str

class Invoice(BaseInvoice):
    invoiceId: int
    
    class Config:
        orm_mode = True

class InvoiceCreate(BaseInvoice):
    pass
