import sqlite3
import pandas as pd

con = sqlite3.connect("../data/data.sqlite")
df = pd.read_sql_query("SELECT * FROM data;", con)

# Filter out the periods of events that happened in Erlangen

events = [
    ('2023-05-25', '2023-06-05'), # Bergkirchweih
    ('2023-10-21', '2023-10-21'), # Lange Nacht der Wissenschaft
    ('2023-11-25', '2023-12-23'), # Weihnachtsmarkt
    ('2024-05-16', '2024-05-27'), # Bergkirchweih
    ('2024-05-30', '2024-06-02')  # Internationaler Comic Salon
]
index_list = []
for event in events:
    temp_list = df['date'][(df['date'] >= event[0]) & (df['date'] <= event[1])].index.tolist()
    index_list += temp_list
df.drop(df.index[index_list], inplace = True)

# Calculate the median of the column pedestrians for every weekday in the data

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['weekday'] = pd.to_datetime(df['date']).dt.day_name()
medians = {}
for i in weekdays:
    medians[i] = df[df['weekday'] == i]['pedestrians'].median()

# Select the rows where the number of pedestrians has a difference of more than 10 % to the respective median of that weekday
more_than_median = []
less_than_median = []
for i in weekdays:
    more_than_median.append(df[(df['weekday'] == i) & (df['pedestrians'] > medians[i] * 1.1)])
    less_than_median.append(df[(df['weekday'] == i) & (df['pedestrians'] < medians[i] * 0.9)])
more_than_median_df = pd.concat(more_than_median).sort_index()
avg_temp_mtm = more_than_median_df['temp'].mean()
avg_rain_mtm = more_than_median_df['rain'].mean()
less_than_median_df = pd.concat(less_than_median).sort_index()
avg_temp_ltm = less_than_median_df['temp'].mean()
avg_rain_ltm = less_than_median_df['rain'].mean()

print()
print("Statistics for the days where the number of pedestrians has a difference\nof more than 10 % to the respective median of that weekday.")
print()
print("Days with more than 10 % above the median:")
print("Average temperature: " + str(round(avg_temp_mtm, 2)) + " °C")
print("Average rainfall:    " + str(round(avg_rain_mtm, 2)) + " mm")
print()
print("Days with more than 10 % below the median:")
print("Average temperature: " + str(round(avg_temp_ltm, 2)) + " °C")
print("Average rainfall:    " + str(round(avg_rain_ltm, 2)) + " mm")
print()
