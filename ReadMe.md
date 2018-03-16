# What

This repo contains a docker file and data for Road Safety published by Government of United Kingdom. The data used here (Road Safety Data) was published by Department of Transport, Government of U.K.

The dockerfile creates a `postgres:latest` container and creates several tables in the database. The central table is the `accidents_2016`. This has several foreign keys, some that refer to the tables generated using the codebook provided by GUK. 

The codebook is called `Road-Accident-Safety-Data-Guide.xls` and an Excel workbook containing multiple sheets, each refering to integer codes used in some of columns in the dataset. Each worksheet (except the "Introduction") worksheet has been converted into individual csv files using the python script `convert_codebook_to_csv.py`, all of which will be uploaded to the database as individual tables.

Data can be obtained from: https://data.gov.uk/dataset/road-accidents-safety-data

# Why

While trying to build dashboards with the dataset using Tableau (for Mac), Tableau kept crashing (without throwing a debug message). After scouring the web for such issues, I wasn't able to figure out why.

In the past, I have had no trouble using Tableau with Database based data sources, which I suspect is due to the fact that all the joins are executed by the database when executing my SQL query. Which is why, I decided to setup a docker container running postgresql 10 and having Tableau connect to that. 

# What can you use this for?

For whatever you want. What does this repo/setup use:
* Docker CE
* PostgreSQL
* Data - published by Government of UK under Open Government License. 

Clone this repo and run the following:

```sh
cd \path\to\repo
docker build -t ukaccidents2016 .
docker run -p 5432:5432 ukaccidents2016 
```
