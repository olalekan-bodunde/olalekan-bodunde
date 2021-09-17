USE airpollutiondb;
SELECT pollutionrecords.`station_id SITE_ID`,pollutionrecords.`id DATE_TIME`,avg(NO2), AVG(NO) FROM pollutionrecords
where pollutionrecords.`id DATE_TIME` >="2010-01-01 O6:00:00" AND `id DATE_TIME` < "2019-12-31 23:59:00"
GROUP BY pollutionrecords.`station_id SITE_ID`
