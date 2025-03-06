import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_pokemon():
    response = requests.get(f"{BASE_URL}?limit=15")
    return response.json()

def fetch_pokemon_details(pokemon_id):
    """Fetch detailed stats for a given Pokémon ID"""
    response = requests.get(f"{BASE_URL}{pokemon_id}")
    return response.json()

if __name__ == "__main__":
    data = fetch_pokemon()
    print(data)
