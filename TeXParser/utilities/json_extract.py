from collections import defaultdict
import requests

def requestJSONData(url: str) -> dict:
    return requests.get(url).json()

def parseJSONData(data: dict, table: str) -> defaultdict:
    if table not in data:
        raise ValueError(f"Table '{table}' not found in the JSON data.")

    row_data = data[table]['rows']
    column_data = data[table]['columns']

    parsed_data = defaultdict(lambda: None)
    parsed_data['row_names'] = tuple(column_data)
    parsed_data['row_entries'] = [tuple(row) for row in row_data]
    parsed_data['col_len'] = len(column_data)
    parsed_data['row_len'] = len(row_data)

    return parsed_data