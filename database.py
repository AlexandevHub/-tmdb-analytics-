import sqlite3
import pandas as pd

DB_NAME = "filmes.db"

def salvar_filmes(df: pd.DataFrame):
    with sqlite3.connect(DB_NAME) as conexao:
        df.to_sql("filmes", conexao, if_exists="replace", index=False)
    print(f"{len(df)} filmes salvos no banco de dados.")

def carregar_filmes() -> pd.DataFrame:
    with sqlite3.connect(DB_NAME) as conexao:
        df = pd.read_sql("SELECT * FROM filmes", conexao)
    return df