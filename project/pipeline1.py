import http.client
import urllib.parse
import json
from datetime import datetime, timedelta
import pandas as pd

conn = http.client.HTTPSConnection("static.hystreet.com")

# For grading please contact me and I will provide you with the correct API token.
# The grenerated csv file is stored in the csv_files folder and can be used with older data as well.
# In that case please comment the call of this script in the pipeline.sh file.

apiKeyFile = open('hystreet.key', 'r')
apiKey = apiKeyFile.readline().rstrip()

headers = {
    'Content-Type': "application/json",
    'X-API-Token': apiKey
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

data_extracted = [
    {
        "timestamp": datetime.fromisoformat(entry["timestamp"][:-6]).strftime("%Y%m%d"),
        "pedestrians_count": entry["pedestrians_count"]
    }
    for entry in measurements
]

df = pd.DataFrame(data_extracted)
df.to_csv('csv_files/PedData.csv', encoding='utf-8', index=False, sep=';')
