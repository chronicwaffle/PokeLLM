import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)
cur = conn.cursor()
print("connected");

def insert_pokemon(pokemon_data):
    cur.executemany("INSERT INTO pokemon (id, name, type1, type2, base_experience) VALUES (%s, %s, %s, %s, %s)", pokemon_data)
    conn.commit()

if __name__ == "__main__":
    from extract import fetch_pokemon
    from transform import transform_pokemon

    raw_data = fetch_pokemon()
    transformed_data = transform_pokemon(raw_data)
    insert_pokemon(transformed_data)
    print("INSERT SUCCESS")

cur.close()
conn.close()