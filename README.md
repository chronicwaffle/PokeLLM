# Pokémon Database Setup and Usage

## Prerequisites

- [Docker](https://www.docker.com/) installed on your system

## Getting Started

### 1. Spin Up the a Docker container from the PostgreSQL image in docker-compose.yaml

```sh
cd docker
docker-compose up -d
```
### 2. Start an Interactive Terminal with psql
```sh
docker exec -it pokemon-db psql -U admin -d pokemon
```

### 3. Query the database
```sql
SELECT * from pokemon WHERE type='grass';
```
**Note:** Don't forget the `;`

### 4. Exit psql
```sh
\q
```

### 5. Stop the container and remove associated volumes.
```sh
docker-compose down -v
```

Now you're set up to manage and query your Pokémon database! 🚀