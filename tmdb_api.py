import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

def buscar_generos() -> dict:
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {"api_key": API_KEY, "language": "pt-BR"}
    response = requests.get(url, params=params).json()
    return {g["id"]: g["name"] for g in response["genres"]}

def buscar_filmes_populares(paginas: int = 5) -> pd.DataFrame:
    url = "https://api.themoviedb.org/3/movie/popular"
    todos_filmes = []

    for pagina in range(1, paginas + 1):
        params = {"api_key": API_KEY, "language": "pt-BR", "page": pagina}
        response = requests.get(url, params=params)
        todos_filmes.extend(response.json()["results"])

    mapa_generos = buscar_generos()

    df = pd.DataFrame(todos_filmes)
    df = df[["title", "release_date", "vote_average", "vote_count", "popularity", "genre_ids"]]
    df["release_date"] = pd.to_datetime(df["release_date"])
    df["genero_principal"] = df["genre_ids"].apply(
        lambda ids: mapa_generos.get(ids[0], "Desconhecido") if ids else "Desconhecido"
    )
    df = df.drop(columns=["genre_ids"])  # remove a lista, já extraímos o que precisava dela
    return df