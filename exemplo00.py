import requests
from pydantic import BaseModel


class PokemonSchame(BaseModel): # Contrato de dados, schema de dados, a view
    name: str
    type: str

    class Config:
        orm_mode = True


def pegar_pokemon(id: int):
    URL = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(URL)

    data = response.json()
    data_types = data['types'] # Supondo que data e dicionario com os dados

    type_list = []
    for type_info in data_types:
        type_list.append(type_info['type']['name'])
    types = ', '.join(type_list)

    return PokemonSchame(name=data['name'], type=types)


if __name__ == "__main__":
    print(pegar_pokemon(10))
    print(pegar_pokemon(6))
    print(pegar_pokemon(13))