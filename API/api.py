from typing import Union

from fastapi import FastAPI
# from pydantic import BaseModel

app = FastAPI()


# model = load('path to model')


@app.get("/")
def read_root():
    return "OK"

@app.get("/user/{user_id}")
def get_recomendaction(user_id: int):
    # Calcular los scores de todas las películas que el user_id no vio
    # Query DB de scores
    # Llamando al modelo

    return [
        {
            'name': 'Titanic',
            'rating': 4.2
        },
        {
            'name': 'Harry Potter',
            'rating': 4.1
        },
        {
            'name': 'Star Wars',
            'rating': 4.0
        }
    ]
    

@app.post("/movies/{item_id}")
def get_similar_movies(movie_id: int, item: str):
    # Llamar a db vectorial para buscar IDs cercanos
    # Con los IDs llamar a la db relacional para buscar los campos de nombre, año, url, etc
    return [
        {   
            'name': 'Titanic',
            'score': 0.98
        },
        {
            'name': 'Harry Potter',
            'score': 0.95
        },
        {
            'name': 'Star Wars',
            'score': 0.93
        }
    ]

@app.post("/movies/{item_id}")
def new_user(user_id: int, item: str):
    pass
