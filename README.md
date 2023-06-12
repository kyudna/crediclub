<div align="center">
    <h1>Crediclub Tech Test</h1>
</div> 

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











