from fastapi import FastAPI, Depends, UploadFile, HTTPException, File
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from services import databaseService, invoiceService
from schemas import invoiceSchema

import os

databaseService.addTables()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "pagos.xlsx")

app = FastAPI()

@app.get("/api/invoices/", response_model=list[invoiceSchema.Invoice])
def getAllInvoices(db: Session = Depends(databaseService.getDB)):
    return invoiceService.getAllInvoices(db=db)

@app.get("/api/invoices/{invoiceSupplierName}", response_model=list[invoiceSchema.Invoice])
def getAllInvoicesBySupplier(invoiceSupplierName: str, db: Session = Depends(databaseService.getDB)):
    return invoiceService.getAllInvoicesBySupplier(db=db, invoiceSupplierName=invoiceSupplierName)

@app.get("/api/paids")
def getAllPaidsReceived(db: Session = Depends(databaseService.getDB)):
    return invoiceService.getAllPaidsReceived(db=db)

@app.post("/api/invoices/", response_model=invoiceSchema.Invoice)
def createInvoice(invoice: invoiceSchema.InvoiceCreate, db: Session = Depends(databaseService.getDB)):
    return invoiceService.createInvoice(db=db, invoice=invoice)

@app.post("/api/upload/", response_model=list[invoiceSchema.Invoice])
def uploadExcel(file: UploadFile = File(...), db: Session = Depends(databaseService.getDB)):
    if not file:
        raise HTTPException(status_code = 400, detail = "No file sent")
    elif file.filename.endswith('.xlsx'):
        return invoiceService.createInvoiceFromExcel(db=db, file=file)
    else:
        raise HTTPException(status_code = 406, detail = "Invalid file extension")

@app.get("/api/download/", response_class=FileResponse)
def downloadExcel(db: Session = Depends(databaseService.getDB)): 
    return invoiceService.downloadExcel(db=db, pathPagosCSV=DOWNLOAD_DIR)
