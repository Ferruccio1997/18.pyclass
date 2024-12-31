import requests
from db import SessionLocal, engine, Base
from models import Pokemon
from schema import PokemonSchema


Base.metadata.create_all(bind=engine)

def fetch_pokemon_data(pokemon_id: int):
    URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        data_types = data['types'] # Supondo que data e dicionario com os dados
        type_list = []
        for type_info in data_types:
            type_list.append(type_info['type']['name'])
        types = ', '.join(type_list)

        return PokemonSchema(name=data['name'], type=types)

    else:
        return None

def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)

    return db_pokemon