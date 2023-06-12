from models import invoiceModel
from numpy import append
import pandas as pd
from fastapi import HTTPException, status
from datetime import datetime

def formatDate(dateToFormat: str):
    finalDate = datetime.strptime(dateToFormat, '%Y-%m-%d')
    return finalDate
    
def processData(file):
    df = pd.read_excel(file)
    invoices = []

    if(df.empty):
        raise HTTPException(status_code = 406, detail = "The excel can't be empty")
    else:
        for i in range(len(df)):
            if(len(df.loc[i, "Fecha"]) == 0 or
               len(df.loc[i, "Cliente"]) == 0 or
               len(df.loc[i, "Monto"]) == 0 or
               len(df.loc[i, "Proveedor"] == 0)):
            
               raise HTTPException(status_code = 406, detail = "Emtpy value detected, please check")
            
            elif(df.loc[i, "Monto"] == str ):

               raise HTTPException(status_code = 406, detail = "The value of Mount can't be a text")

            else:
                try:
                    invoice = invoiceModel.Invoice(
                        invoiceDate = formatDate(df.loc[i, "Fecha"]),
                        invoiceClient = df.loc[i, "Cliente"],
                        invoiceMount = df.local[i, "Monto"],
                        invoiceSupplier = df.local[i, "Proveedor"]
                    )
                    invoices.append(invoice)
                except:
                    raise HTTPException(status_code = 500, detail = "Something fail")

        return invoices
