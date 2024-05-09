# Create a network

Run:

- `docker network create pgdatabase`

# To persist data

Create volumes for postgres and pgadmin using:

- `docker volume create msqdata`

# To start the MySQL server

From the command line run: `docker compose up -d`

# To connect to the server

You can use MySQLWorkbench or adminer to connect to the server

The settings should look like:

- Hostname: 127.0.0.1
- port: 3306
- username: root
- password is the docker-compose file. This should be changed to use an environment variable if used in production
