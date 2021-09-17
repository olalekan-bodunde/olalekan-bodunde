USE airpollutiondb;
SELECT station.`id SITE_ID`, station.LOCATION, pollutionrecords.`id DATE_TIME`, MAX(CO) AS HIGHEST_CO 
FROM airpoldb.pollutionrecords, airpoldb.station