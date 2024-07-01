import sqlite3

# connect to the database
con = sqlite3.connect("../data/data.sqlite")
 
# The following manipulations are done in SQL
# As the temperature and rain data are stored in two different tables, the data is combined in two subqueries
# The average of the temperature and rain data is calculated and a column with row numbers is added to the tables
# The two subqueries are joined together with thew table 'pedestrians' and the columns 'date', 'pedestrians', 'rain' and 'temp' are selected

p = con.cursor()

# Create a new table 'data' with the columns 'date', 'pedestrians', 'rain' and 'temp' into the database 'data.sqlite'
p.execute('''
CREATE TABLE data (
    date TEXT,
    pedestrians INTEGER,
    rain REAL,
    temp REAL
);
''')
con.commit()

# Insert the data into the table 'data'
p.execute('''

WITH RainData AS (
    SELECT
        r1.MESS_DATUM AS date,
        round((r1.[  RS] + r2.[  RS]) / 2, 2) AS rain
    FROM rainmoe r1
    JOIN rainnue r2 ON r1.MESS_DATUM = r2.MESS_DATUM
),
TempData AS (
    SELECT
        t1.MESS_DATUM AS date,
        round((t1.[ TMK] + t2.[ TMK]) / 2, 2) AS temp
    FROM tempmoe t1
    JOIN tempnue t2 ON t1.MESS_DATUM = t2.MESS_DATUM
)

INSERT INTO data SELECT
    pd.timestamp AS date,
    pd.pedestrians_count AS pedestrians,
    rd.rain,
    td.temp
FROM pedestrians pd
JOIN RainData rd ON pd.timestamp = rd.date
JOIN TempData td ON pd.timestamp = td.date;
''')
con.commit()

print("[Pipeline3] Table 'data' has been created and the pedestrians data merged with the averaged weather data has been inserted.")

# Update the string representation of the dates in the table 'data' to the format 'YYYY-MM-DD'
p.execute('''

UPDATE data
SET date = SUBSTR(date, 1, 4) || '-' || SUBSTR(date, 5, 2) || '-' || SUBSTR(date, 7, 2)
WHERE LENGTH(date) = 8;

''')
con.commit()

print("[Pipeline3] The String representation of the dates in the table 'data' has been updated.")

p.close()
