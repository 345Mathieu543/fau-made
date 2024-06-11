from datetime import datetime, timedelta
import pandas as pd
import urllib.parse
import http.client
import json
import pytz
import re

def get_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.readline().rstrip()

def fetch_data(start, end, headers):
    conn = http.client.HTTPSConnection("static.hystreet.com")
    body = f"from={start}&to={end}&resolution=day"
    conn.request("GET", f"/api/https://api.hystreet.com/locations/142?{body}", headers=headers)
    res = conn.getresponse()
    return res.read()

def parse_data(data):
    parsed = json.loads(data.decode("utf-8"))
    measurements = parsed['measurements']
    return [
        {
            "timestamp": datetime.fromisoformat(entry["timestamp"][:-6]).strftime("%Y%m%d"),
            "pedestrians_count": entry["pedestrians_count"]
        }
        for entry in measurements
    ]

def save_to_csv(data, file_path):
    df = pd.DataFrame(data)
    df.to_csv(file_path, encoding='utf-8', index=False, sep=';')

def adjust_dates_if_needed(startdate, enddate, cet):
    current_time = datetime.now(pytz.timezone('CET'))
    cutoff_time = datetime.combine(current_time.date(), datetime.min.time()).replace(tzinfo=pytz.timezone('CET')) + timedelta(hours=11, minutes=35)
    if current_time < cutoff_time:
        startdate -= timedelta(days=1)
        enddate -= timedelta(days=1)
    return startdate, enddate

def update_file(file_path, pattern, replacement):
    with open(file_path, 'r') as file:
        content = file.read()
    modified_content = re.sub(pattern, replacement, content)
    with open(file_path, 'w') as file:
        file.write(modified_content)

def main():

    # Fetching the pedestrians data from the API
    
    headers = {
        'Content-Type': "application/json",
        'X-API-Token': get_api_key('hystreet.key')
    }
    
    cet = pytz.timezone("CET")
    enddate = datetime.now() - timedelta(days=1)
    startdate = enddate - timedelta(days=549)
    
    start = urllib.parse.quote_plus(cet.localize(startdate.replace(hour=0, minute=0, second=0)).strftime("%Y-%m-%dT%H:%M:%S%z"))
    end = urllib.parse.quote_plus(cet.localize(enddate.replace(hour=23, minute=59, second=59)).strftime("%Y-%m-%dT%H:%M:%S%z"))
    
    # print(f"Start date: {start}")
    # print(f"End date: {end}")
    
    data = fetch_data(start, end, headers)
    data_extracted = parse_data(data)
    save_to_csv(data_extracted, 'csv_files/PedData.csv')
    
    print("[Pipeline1] Pedestrians data extracted and saved to 'csv_files/PedData.csv'.")
    
    # Preparation of the pipeline2.jv file
    pattern = r'(?<=(nieder|_klima)_tag_).*_.*(?=_[0-9]{5}\.txt)'
    startdate, enddate = adjust_dates_if_needed(startdate, enddate, cet)
    newstart = cet.localize(startdate).strftime("%Y%m%d")
    newend = cet.localize(enddate).strftime("%Y%m%d")
    replacement = f'{newstart}_{newend}'
    # print(replacement)
    
    update_file('pipeline2.jv', pattern, replacement)
    
    print("[Pipeline1] Filenames for 'pipeline2.jv' have been adapted successfully.")

if __name__ == "__main__":
    main()
