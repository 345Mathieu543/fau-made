import http.client
import urllib.parse
import json
from datetime import datetime, timedelta
import pandas as pd

conn = http.client.HTTPSConnection("static.hystreet.com")

headers = {
    'Content-Type': "application/json",
    'X-API-Token': "<API-TOKEN>"
    }

enddate = datetime.now() - timedelta(days=1)
startdate = enddate - timedelta(days=549)

start = urllib.parse.quote_plus(startdate.strftime("%Y-%m-%dT%H:%M:%S%z"))
end = urllib.parse.quote_plus(enddate.strftime("%Y-%m-%dT%H:%M:%S%z"))

body = f"from={start}&to={end}&resolution=day"

conn.request("GET", f"/api/https://api.hystreet.com/locations/142?{body}", headers=headers)

res = conn.getresponse()
data = res.read()

parsed = json.loads(data.decode("utf-8"))
measurements = parsed['measurements']

# Extract only the required columns
data_extracted = [
    {
        "timestamp": datetime.fromisoformat(entry["timestamp"][:-6]).strftime("%Y%m%d"),
        "pedestrians_count": entry["pedestrians_count"]
    }
    for entry in measurements
]

df = pd.DataFrame(data_extracted)
df.to_csv('csv_files/PedData.csv', encoding='utf-8', index=False, sep=';')
