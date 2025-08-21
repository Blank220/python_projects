import requests

base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url = f'{base_url}/pokemon/{name}'
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        print('Data retrieved!')
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f'Failed to retrieve data{response.status_code}')


pokemon_name = input('Choose Your Pokemon!: ')
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    poke_name = f'Name: {pokemon_info['name'].title()}'
    poke_id = f'Id: {pokemon_info['id']}'
    poke_height = f'{pokemon_info['height']}'
    poke_weight = f'{pokemon_info['weight']}'
    poke_type = f'{pokemon_info['types']}'

    print(poke_name)
    print(poke_id)
    print(f"Height: {int(poke_height) * .1:.2f}m")
    print(f'Weight: {int(poke_weight) / 10:.2f}kg')
    print(poke_type)


