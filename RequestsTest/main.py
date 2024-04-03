import requests

host_name = 'https://api.pokemonbattle.me/v2'
trainer_token = 'b7434b21f5324356a08cec74b143c8db'
trainer_id = 2500

response = requests.post(
    url = host_name + '/pokemons',
    headers = {'Content-Type': 'application/json',
               'trainer_token': trainer_token},
    json = {"name": "Бумбараш",
            "photo": "https://dolnikov.ru/pokemons/albums/001.png"}
)
print ('Создан покемон: ', response.json())

pokemon_id = response.json() ["id"]

response = requests.put(
    url = host_name + '/pokemons',
    headers = {'Content-Type': 'application/json',
               'trainer_token': trainer_token},
    json = {
            "pokemon_id": pokemon_id,
            "name": "Проходимец",
            "photo": "https://dolnikov.ru/pokemons/albums/001.png"
            }
)
print ('Заменили имя на Проходимец: ', response.json())

response = requests.post(
    url = host_name + '/trainers/add_pokeball',
    headers = {'Content-Type': 'application/json',
               'trainer_token': trainer_token},
    json = {
            "pokemon_id": pokemon_id,
            }
)
print(f"Покемон {pokemon_id} пойман в покебол: {response.json()}")
