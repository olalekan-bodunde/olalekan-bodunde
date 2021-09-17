# Student number: 20053036

# importing libraries
import pandas as pd
import numpy as np
import mysql.connector

# establishing connection to database
mydb = mysql.connector.connect(host = "localhost",
                              user = "root",
                              database = "airpollutiondb")
cursor = mydb.cursor(prepared = True)    # creating cursor

# importing csv
df = df = pd.read_csv("Bristol-air-quality-data-Updated_cleaned.csv", low_memory=False)
# pulling out specific columns needed to populate the station table from the csv
station = df[["SITE_ID", "LOCATION", "GEO_POINT_2D"]]
station = station.drop_duplicates()
print(station)

# converting dataframe to a list of tuples
records_list_1 = list(zip(*map(station.get, station)))
print(records_list_1)

# sql query statement
sql_query = "INSERT INTO station (`id SITE_ID`, LOCATION, `GEO_POINT_2D`) VALUES (%s,%s,%s)"

cursor.executemany(sql_query, records_list_1)     # executing query

# commiting changes to database
mydb.commit()
print("Done, data successfully committed")
cursor.close()                                      # closing connection to database
mydb.close()
print("database closed succesfully")

print("populating pollution records table now............")
# populating pollution records table
mydb = mysql.connector.connect(host = "localhost",               
                              user = "root",                     # re-establishing connection to database
                              database = "airpollutiondb")
cursor = mydb.cursor(prepared = True)

# pulling out specific columns needed to populate pollution records table from the csv
records = df[["DATE_TIME", "NOx", "NO2", "NO", "PM10", "NVPM10", "VPM10", "PM2.5","NVPM2.5", 
              "VPM2.5", "SO2", "O3","CO", "DATE_START", "DATE_END", "TEMPERATURE", "RH","AIR_PRESSURE",
              "CURRENT","INSTRUMENT_TYPE","SITE_ID"]]
records = records.drop_duplicates()

# converting the dataframe records to a list of tuples
records_list_1 = list(zip(*map(records.get, records)))

# my sql query statement
sql_query = """INSERT INTO pollutionrecords
(`id DATE_TIME`, NOx, NO2, NO, PM10, NVPM10, VPM10, `PM2.5`,`NVPM2.5`, 
              `VPM2.5`, SO2, O3,CO, DATE_START, DATE_END, TEMPERATURE, RH,AIR_PRESSURE,
              CURRENT,INSTRUMENT_TYPE,`station_id SITE_ID`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

# executing query
cursor.executemany(sql_query, records_list_1)

mydb.commit()                                  # commiting changes to database
print("Done, data successfully committed")
cursor.close()                                     # closing connection to database
mydb.close()
print("database closed succesfully")
