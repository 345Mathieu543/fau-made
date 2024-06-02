import sqlite3

# connect to the database
con = sqlite3.connect("../data/data.sqlite")
 
# The following manipulations are done in SQL
# As the temperature and rain data are stored in two different tables, the data is combined in two subqueries
# The average of the temperature and rain data is calculated and a column with row numbers is added to the tables
# The two subqueries are joined together with thew table 'pedestrians' and the columns 'date', 'pedestrians', 'rain' and 'temp' are selected

# Create a new table 'data' with the columns 'date', 'pedestrians', 'rain' and 'temp' into the database 'data.sqlite'
p = con.cursor()
p.execute('''
CREATE TABLE data (
    date INTEGER,
    pedestrians INTEGER,
    rain REAL,
    temp REAL
);
''')

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
