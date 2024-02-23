from collections import defaultdict
import requests

def requestJSONData(url: str) -> dict:
    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError(f"Failed to retrieve JSON data from '{url}'. Status code: {response.status_code}")
    return response.json()

def parseJSONData(data: dict, table: str) -> defaultdict:
    if table not in data:
        raise ValueError(f"Table '{table}' not found in the JSON data.")

    row_data = data[table]['rows']
    column_data = data[table]['columns']

    parsed_data: defaultdict | None = defaultdict(lambda: None)

    # Skip the row entries in column 'Code'
    parsed_data['col_names'] = column_data[1:]
    parsed_data['row_entries'] = [row[1:] for row in row_data]

    parsed_data['col_len'] = len(column_data) - 1
    parsed_data['row_len'] = len(row_data)

    return parsed_data

print(requestJSONData("http://localhost/TeXParser/json_test.php"))