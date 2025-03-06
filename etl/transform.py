from extract import fetch_pokemon_details

def transform_pokemon(data):
    transformed_data = []

    for p in data['results']:
        pokemon_id = int(p['url'].split("/")[-2])  # Extract Pokémon ID from URL

        # Fetch detailed Pokémon data from PokéAPI
        poke_details = fetch_pokemon_details(pokemon_id)  # Call helper function

        name = poke_details.get('name', 'Unknown')
        base_experience = poke_details.get('base_experience', 0)

        # Extract type(s) (Some Pokémon have 2 types, others have 1)
        types = poke_details.get('types', [])
        type1 = types[0]['type']['name'] if len(types) > 0 else None
        type2 = types[1]['type']['name'] if len(types) > 1 else None

        # Add data
        transformed_data.append((pokemon_id, name, type1, type2, base_experience))

    return transformed_data