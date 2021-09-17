# importing libraries
import pandas as pd

df = df = pd.read_csv("Bristol-air-quality-data-Updated_cleaned.csv", low_memory=False)

Table_name = "station"              # table names
Table_name_2 = "Pollution"

# looping through csv to generate insert statement
with open("pollution_data.sql", "w"):                # opening new .sql file
    for index, row in df.iterrows():
        print("INSERT INTO" +"",Table_name + "(\"SITE_ID\",\"LOCATION\",\"GEOM_POINT_2D\"), VALUES (", row["SITE_ID"],
                  ",", row["LOCATION"],",", row["GEO_POINT_2D"] +"\");", file=open("pollution_data.sql", "a"))
        
with open("pollution_data.sql", "a"):
    for index, row in df.iterrows():
        print("INSERT INTO"+"", Table_name_2 + "(\"DATE_TIME\",\"NOx\",\"NO\",\"NO2\",\"PM10\",\"NVPM10\",\"VPM10\",\"PM2.5\",\"NVPM2.5\",\"VMP2.5\",\"SO2\",\"O3\",\"CO\",\"DATE_START\",\"DATE_END\",\"TEMPERATURE\",\"RH\",\"AIR_PRESSURE\"), VALUES(", row["DATE_TIME"],
                  ",", row["NOx"],",", row["NO"],",", row["NO2"],",", row["PM10"],",", row["NVPM10"],",", row["VPM10"],",", row["PM2.5"],",", row["NVPM2.5"],",", row["VPM2.5"],",", row["CO"],",", row["O3"],",", row["SO2"],",", row["TEMPERATURE"],",", row["RH"],",", row["AIR_PRESSURE"],
              ",", row["DATE_START"], ",", str(row["DATE_END"]) +"\");", file=open("pollution_data.sql", "a"))
        
    
           

