from models import invoiceModel

import pandas as pd
from fastapi import HTTPException
from datetime import datetime, date

def formatDateToDatabase(dateToFormat: str):
    finalDate = datetime.strftime(pd.to_datetime(dateToFormat).date(), '%Y-%m-%d')
    return finalDate

def formatDateToUser(dateToFormat: str):
    finalDate = datetime.strftime(pd.to_datetime(dateToFormat).date(), '%d/%m/%Y')
    return finalDate

def processData(file):
    df = pd.read_excel(file.file.read())

    invoices = []
    invoicesColumns = ["Fecha", "Cliente", "Monto", "Proveedor"]
    if(df.empty):
        raise HTTPException(status_code = 406, detail = "The excel can't be empty")
    else:
        if invoicesColumns != list(df.columns.values):
            raise HTTPException(status_code = 406, detail = "Columns names dont match: " + str(list(df.columns.values)))
        
        for i in range(len(df)):
            if(len(str(df.loc[i, "Fecha"])) == 0 or
               len(df.loc[i, "Cliente"]) == 0 or
               len(str(df.loc[i, "Monto"])) == 0 or
               len(str(df.loc[i, "Proveedor"])) == 0):
            
               raise HTTPException(status_code = 406, detail = "Emtpy value detected, please check")
            
            elif(type(df.loc[i, "Monto"])== str):
               raise HTTPException(status_code = 406, detail = "The value of Mount can't be a text")
            else:
                try:
                    invoice = invoiceModel.Invoice(
                        invoiceDate = formatDateToDatabase(str(df.loc[i, "Fecha"])),
                        invoiceClient = df.loc[i, "Cliente"],
                        invoiceMount = df.loc[i, "Monto"],
                        invoiceSupplier = df.loc[i, "Proveedor"]
                    )
                    
                    invoices.append(invoice)
                except:
                    raise HTTPException(status_code = 500, detail = "Something fail")
        return invoices
