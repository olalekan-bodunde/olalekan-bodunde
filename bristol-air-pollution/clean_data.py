# student number: 20053036

import pandas as pd

data = pd.read_csv('air-quality-data.updated.csv',
                   sep=';',
                   low_memory=False)
#print(data.info())
# filtering the data and dealing with mismatch
siteid = data["SiteID"]
site_ids = []
for i in siteid:
    if i not in site_ids:  # gets the unique siteid without repitition
        site_ids.append(i)
print(site_ids)
print("There are" + "",  len(site_ids), ""+ "record of site ids, which includes the mismatch and null values as shown in the list above" )
invalid_siteid = data.loc[data['SiteID'] == 573.0]
data.drop(invalid_siteid.index, inplace=True)
print("There are" + "",len(invalid_siteid), ""+ "lines of records with invalid site_id number 573.0")
# pulling out just siteid and location column in order to check for mismatch
site_loc = data[["SiteID", "Location"]]
# print(site_loc)
site452 = site_loc[site_loc['SiteID'] == 452.0]  # print siteid and location = aurn st paul
# 452 and 270 has a mismatch
# print(site452)
location452 = site452['Location']
# print(location452)
# getting individual entry in location without duplicate
location_list = []
for stations in location452:
    if stations == "Wells Road":
        location_list.append(stations)  # finds out how many wells road shares same site id with aurn st paul
invalid_loc = site452[site452['Location'] == "Wells Road"]
print("There is" + "", len(invalid_loc), ""+ "location with a wrong siteid")
# print(invalid_loc)
data.drop(invalid_loc.index, inplace=True)
# filtering out all null values in SiteID
(data.SiteID.isnull()).value_counts()
null_siteid = data[data.SiteID.isnull()]
data.drop(null_siteid.index, inplace=True)
print("There are" + "", len(null_siteid), ""+ "records with null site_id in the data")
print("IN TOTAL," + "", len(null_siteid)+len(invalid_siteid)+len(invalid_loc), ""+ "ROWS WERE FILTERED OUT OF THE DATA")

# Renaming the columns for consistency
data.rename(columns={'Date Time': 'DATE_TIME', "SiteID": "SITE_ID", 'Temperature': "TEMPERATURE",
                        "Air Pressure": "AIR_PRESSURE", "Location": "LOCATION",
                        "geo_point_2d": "GEO_POINT_2D", "DateStart": "DATE_START",
                        "DateEnd": "DATE_END", "Current": "CURRENT", "Instrument Type": "INSTRUMENT_TYPE"},
               inplace=True)
clean_data = data.to_csv("Bristol-air-quality-data-Updated_cleaned.csv", index=False)
clean_data = pd.read_csv("Bristol-air-quality-data-Updated_cleaned.csv",
                   sep=',',
                   low_memory=False)
print("There are" + "", len(clean_data), "" + " rows and", len(clean_data.columns),
      "" + "columns written to cleaned csv")

