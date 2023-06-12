from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile
from fastapi.responses import StreamingResponse, FileResponse

from models import invoiceModel
from schemas import invoiceSchema
from utils import invoiceUtil

from datetime import datetime
import os

import pandas as pd

def getAllInvoices(db: Session):
    return db.query(invoiceModel.Invoice).all()

def getAllInvoicesBySupplier(invoiceSupplierName: str, db: Session):
    dbInvoices = db.query(invoiceModel.Invoice).filter(invoiceModel.Invoice.invoiceSupplier == invoiceSupplierName)
    
    dbInvoicesList = list(map(invoiceSchema.Invoice.from_orm, dbInvoices))

    if not dbInvoicesList:
        raise HTTPException(status_code = 404, detail = "Invoices for that Supplier not found")

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

def createInvoiceByFile(db: Session, file):
    invoices = invoiceUtil.processData(file)
    db.bulk_insert_mappings(invoiceModel.Invoice, invoices)
    db.commit()
    return invoices

def downloadExcel(db: Session, pathPagosCSV: str):
    invoicesQuery = db.query(invoiceModel.Invoice).all()
    invoicesList = {"Fecha" : [],
                    "Cliente" : [],
                    "Monto" : [],
                    "Proveedor" : []}

    for x in invoicesQuery:
        invoicesList["Fecha"].append(x.invoiceDate)
        invoicesList["Cliente"].append(x.invoiceClient)
        invoicesList["Monto"].append(x.invoiceMount)
        invoicesList["Proveedor"].append(x.invoiceSupplier)

    df = pd.DataFrame.from_dict(invoicesList)
    df.to_csv('pagos.csv', index = False)

    return FileResponse(path = pathPagosCSV, 
                        media_type = "text/csv",
                        headers = {"Content-Disposition" : "attachment; filename = pagos.csv"})
    
    #return StreamingResponse(
            #iter([df.to_csv(index = False)]),
            #media_type = "text/csv",
            #headers = {"Content-Disposition" : f"attachment; filename = pagos.csv"}
            #)




