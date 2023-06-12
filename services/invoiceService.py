from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import FileResponse

from models import invoiceModel
from schemas import invoiceSchema
from utils import invoiceUtil

import pandas as pd

def getAllInvoices(db: Session):
    return db.query(invoiceModel.Invoice).all()

def getAllInvoicesBySupplier(invoiceSupplierName: str, db: Session):
    dbInvoices = db.query(invoiceModel.Invoice).filter(invoiceModel.Invoice.invoiceSupplier == invoiceSupplierName)
    
    dbInvoicesList = list(map(invoiceSchema.Invoice.from_orm, dbInvoices))

    if not dbInvoicesList:
        raise HTTPException(status_code = 202, detail = "Invoices for that Supplier not found")

    return  dbInvoicesList

def createInvoice(db: Session, invoice: invoiceSchema.InvoiceCreate):
    dbInvoice = invoiceModel.Invoice(
            invoiceDate=invoice.invoiceDate,
            invoiceClient=invoice.invoiceClient,
            invoiceMount=invoice.invoiceMount,
            invoiceSupplier=invoice.invoiceSupplier
    )
    db.add(dbInvoice)
    db.commit()
    return dbInvoice

def createInvoiceFromExcel(db: Session, file):
    invoices = invoiceUtil.processData(file)
    for x in invoices:
        db.add(x)
    db.commit()
    return invoices

def downloadExcel(db: Session, pathPagosCSV: str):
    invoicesQuery = db.query(invoiceModel.Invoice).all()
    invoicesQueryList = list(map(invoiceSchema.Invoice.from_orm, invoicesQuery))

    if not invoicesQueryList:
        raise HTTPException(status_code = 202, detail = "No invoices to download")
    
    invoicesList = {"Fecha" : [],
                    "Cliente" : [],
                    "Monto" : [],
                    "Proveedor" : []}
    
    for x in invoicesQuery:
        invoicesList["Fecha"].append(invoiceUtil.formatDateToUser(x.invoiceDate))
        invoicesList["Cliente"].append(x.invoiceClient)
        invoicesList["Monto"].append(x.invoiceMount)
        invoicesList["Proveedor"].append(x.invoiceSupplier)

    df = pd.DataFrame.from_dict(invoicesList)
    df.to_excel('pagos.xlsx', index = False)

    return FileResponse(path = pathPagosCSV, 
                        media_type = 'application/octet-stream',
                        filename = 'pagos.xlsx')




