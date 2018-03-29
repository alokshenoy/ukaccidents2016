UPDATE incidents_2016
SET "Time" = CAST("Time" AS TIME)

UPDATE incidents_2016
SET "Date" = to_date("Date", 'DD/MM/YYYY')

UPDATE incidents_2016
SET "Date" = replace("Date",'0016','2016')


