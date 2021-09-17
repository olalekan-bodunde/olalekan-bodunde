USE airpollutiondb;
SELECT station.`id SITE_ID`, station.LOCATION, station.GEO_POINT_2D, pollutionrecords.`id DATE_TIME`, pollutionrecords.NOx, pollutionrecords.`NO`,
pollutionrecords.NO2, pollutionrecords.PM10,pollutionrecords.NVPM10,pollutionrecords.VPM10,pollutionrecords.`PM2.5`, pollutionrecords.`NVPM2.5`,
pollutionrecords.`VPM2.5`, pollutionrecords.SO2,pollutionrecords.CO, pollutionrecords.O3, pollutionrecords.DATE_START,pollutionrecords.DATE_END,
pollutionrecords.TEMPERATURE,pollutionrecords.RH, pollutionrecords.AIR_PRESSURE, pollutionrecords.`CURRENT`, pollutionrecords.INSTRUMENT_TYPE
FROM airpoldb.pollutionrecords
INNER JOIN station 
ON station.`id SITE_ID` = pollutionrecords.`STATION_id SITE_ID` 
WHERE station.`id SITE_ID` = 203
AND `id DATE_TIME` >="2019-01-01"
AND `id DATE_TIME` < "2020-01-01"