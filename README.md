## Airflow ETL Pipeline – OpenSky Flights Data
# Archtecture

This project implements an end-to-end ETL pipeline using Apache Airflow in a Dockerized environment to process real-time flight data from the OpenSky API. The pipeline follows the Medallion Architecture pattern (Bronze, Silver, and Gold layers) to ensure structured and scalable data processing. In the Bronze layer, raw flight data is extracted from the API and stored as timestamped JSON files, preserving the original dataset as a reliable source of truth. In the Silver layer, the raw data is transformed into a structured format using Pandas, relevant columns such as aircraft identifier, origin country, velocity, and ground status are selected, and the cleaned data is saved as CSV files. In the Gold layer, the dataset is aggregated by origin country to produce business-ready metrics, including total flights, average velocity, and the number of aircraft on the ground. Airflow orchestrates the workflow through sequential tasks and uses XCom to pass file paths between stages. The final processed dataset is prepared for loading into Snowflake, making it suitable for analytics, reporting, and business intelligence use cases.

<img width="1919" height="1054" alt="Screenshot 2026-02-27 234038" src="https://github.com/user-attachments/assets/465a15af-538c-4ffc-880c-5456d5af5c52" />

<img width="1367" height="658" alt="Screenshot 2026-03-01 152913" src="https://github.com/user-attachments/assets/fe0e8ba1-3165-435e-bd3e-7b2f8449030d" />

<img width="1341" height="821" alt="Screenshot 2026-02-28 223833" src="https://github.com/user-attachments/assets/ff7d1733-91e1-42bc-915e-bce2f8e63e7b" />


