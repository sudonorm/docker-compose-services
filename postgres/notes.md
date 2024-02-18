# Postgres database with pgadmin

<strong> Change the credentials in the docker-compose file to fit </strong>

# Usage

## Create a network

Run:

- `docker network create pgdatabase`

## To persist data

Create volumes for postgres and pgadmin using:

- `docker volume create pgdata`
- `docker volume create pgadmindata`

## To connect to the Postgres instance using pgadmin.

Search for the ip address of the Postgres container using:

- `docker inspect <container name or id>`

In the resulting JSON file:

- look for `Networks` (it's usually toward the end)

- within this section, look for the key `IPAddress`

The ip address value here is what will be our hostname in pgadmin.

You can also use:

- `docker inspect <container name or id> | grep IPAddress `

// https://stackoverflow.com/questions/38532483/where-is-var-lib-docker-on-mac-os-x

// configure pgadmin: https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html

The following commands need to be run from a linux shell. You can either use the Ubuntu or you can use a git bash.

### To backup the database running in the container, run:

    docker exec -t <containerid> pg*dump -c -U postgres databaseName | gzip > ./db_dump*$(date +"%Y-%m-%d*%H*%M\_%S").gz

### To restore a backup of the database, run:

    gunzip < <path-to-gz-backup-file> | docker exec -i <containerid> psql -U postgres -d <databaseName>
