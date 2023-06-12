<div align="center">
    <h1>Crediclub Tech Test</h1>
</div> 

> Rest API builded with FastApi  

## Requirements
- Python 3.7+.
- PostgreSQL with a database created for the project.

### Installation
- Clone the repository:
```zsh
git clone https://github.com/xk4i/crediclub.git
```
- Create python venv:
```zsh
python -m venv venv
```
- Activate venv:
1. Windows:
    ```zsh
    venv/Script/activate
    ```
2. Linux:
    ```zsh
    source venv/bin/activate
    ```

### Dependencies
- Install fastapi, sqlalchemy, uvicorn, pyscopg2-binary, pandas, multipart, openpyxl.
```zsh
pip install fastapi sqlalchemy uvicorn psycopg2-binary pandas multipart openpyxl
```

### Configuration
- Open database properties located on `crediclub/config/databaseConfig.py` and change values with your `postgresql` configuration. 

    - `userName` = ""
    - `userPassword` = ""
    - `server` = ""
    - `databaseName` = ""

- Then run this command to activate uvicorn server:
```zsh
uvicorn main:app --reload
```

> Finally, at this point you have running the app locally on `http://127.0.0.1:8000`.

Go to `http://127.0.0.1:8080/docs` to see the front-end API.

![](https://github.com/xk4i/crediclub/blob/main/screenshots/preview.PNG?raw=true)

## Solution

- El problema se abordó analizando primero la estructura que debería tener la base de datos conforme al requerimiento principal, tratando de satisfacer la necesidad al mismo tiempo de simplificar después el proceso de código.

    > Como la estructura de las facturas es la misma `[Fecha, Client, Monto, Proveedor]`, decidí implementar solo una tabla para las mismas.

- Teniendo la base de datos estructurada, se procedió con la estructura y diseño del proyecto, diviendo por capas las necesidades que se iban a requerir para posteriormente empezar con el desarrollo.

    > El principal problema en la parte del desarrollo, fue el subir el archivo con los datos, hacer las validaciones correspondientes y posteriormente hacer un `insert` en la base de datos.

    > Se planteó primero validar que se estuviera subiendo un archivo excel, para posteriormente validar las columnas, si las columnas no eran las propuestas, se enviaría un error `406`, explicando que las columnas no concuerdan.

    > Para finalizar, se validaron los datos por fila para después crear una lista con los modelos, `agregando` a la cola del engine los modelos a insertar, para posteriormente hacer el `commit` base de datos.










