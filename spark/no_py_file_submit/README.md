# Run Spark in a Docker container

## About the Dockerfile and docker-compose.yml:

The Dockerfile and docker-compose.yml were adopted from mrn-aglic's `spark-standalone-cluster`. See below for the GitHub links and a link to the article if some help is needed in getting up and running.

<strong>Be sure to modify the Spark version and URL in the Dockerfile appropriately. Sometimes, the URL changes.</strong>

## Usage:

- Adjust the requirements.txt file as needed. This is located in the `requirements` folder
- If this is supposed to be added to a specific network, be sure to create the network and add it to the `docker-compose.yml` file
- <strong>MUST do</strong>: create a persistent storage for the Spark logs. Run this after starting the Docker engine: `docker volume create spark-logs`
- To run all the services, change to the `no_py_file_submit` directory and run: `docker-compose up -d` after starting the Docker engine
- To run Jupyter notebooks, a Jupyter Lab server is created as a service, which can be used to run the notebooks in the notebooks folder. Be sure to use this server. It's accessible at `localhost:8888`. All notebooks should be placed in the `notebooks` folder
- `Data files` such as csvs, parquet, orc should be placed in the `data` folder. Files can be referenced using: `/opt/spark/data/someFile.csv`
- Open the `spark-connect.ipynb` and try to initialize a Spark session
- If there are no errors, we are good-to-go with using Spark for processing

### Links:

GitHub for single cluster: https://github.com/mrn-aglic/spark-standalone-cluster
GitHub with being able to submit py files from the terminal: https://github.com/mrn-aglic/pyspark-playground

- Article for installing Spark: https://medium.com/@MarinAgli1/setting-up-a-spark-standalone-cluster-on-docker-in-layman-terms-8cbdc9fdd14b
