// Spin up docker container from postgres image in docker-compose.yml
cd docker
docker-compose up -d

// Start an interactive terminal with psql
docker exec -it pokemon-db psql -U admin -d pokemon

// Query the db. Don't forget the ; (!)
SELECT * from pokemon WHERE type='grass';

// Exit psql
\q

// Stop the db
docker-compose down -v