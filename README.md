## Airflow ETL Pipeline – OpenSky Flights Data
# Overview
This project implements an end-to-end ETL pipeline using Apache Airflow (Dockerized) to process real-time flight data from the OpenSky API.
The pipeline follows the Medallion Architecture pattern (Bronze → Silver → Gold) and prepares analytics-ready data for loading into Snowflake.

Tech Stack:
  
 * Python
 * Apache Airflow
 * Docker
 * Pandas
 * Snowflake
 * OpenSky REST API

# Archtecture
<img width="812" height="385" alt="image" src="https://github.com/user-attachments/assets/425b21f7-dbb5-4258-857c-f677fe9eb9c6" />

## Pipeline Layers
# Bronze Layer:

  * Extracts flight data from OpenSky API
  * Stores raw JSON files with timestamps
  * Serves as the source of truth
  * Silver Layer
# Silver Layer:

  * Transforms raw JSON into structured format
  * Selects relevant columns
  * Outputs cleaned CSV files
# Gold Layer:

  * Aggregates data by origin country
  
  * Calculates:

    * Total flights
    
    * Average velocity
    
    * Flights on ground

  * Produces business-ready dataset


# How to Run

 1) Start Airflow with Docker
 
  * docker-compose up --build
 
 2) Open Airflow UI
 
  * http://localhost:8080
    
 3) Enable and trigger the DAG


# Key Features

  * Real-time API data ingestion
  
  * Medallion architecture implementation
  
  * Automated workflow orchestration
  
  * Dockerized development environment
  
  * Cloud data warehouse integration


# Docker
<img width="1919" height="1054" alt="Screenshot 2026-02-27 234038" src="https://github.com/user-attachments/assets/465a15af-538c-4ffc-880c-5456d5af5c52" />
# Airflow
<img width="1367" height="658" alt="Screenshot 2026-03-01 152913" src="https://github.com/user-attachments/assets/fe0e8ba1-3165-435e-bd3e-7b2f8449030d" />
# Snowflake Visualization
<img width="1341" height="821" alt="Screenshot 2026-02-28 223833" src="https://github.com/user-attachments/assets/ff7d1733-91e1-42bc-915e-bce2f8e63e7b" />


