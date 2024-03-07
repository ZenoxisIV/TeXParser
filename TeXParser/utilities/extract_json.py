from collections import defaultdict
from typing import Any
from handle.warnings import NoTableFoundWarning
from handle.checker import check_table
import requests

def requestJSONData(url: str) -> dict[str, Any]:
    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError(f"Failed to retrieve JSON data from '{url}'. Status code: {response.status_code}")
    return response.json()

def parseJSONData(data: dict[str, Any], table: str) -> defaultdict[str, Any] | None:
    if check_table(data, table, NoTableFoundWarning):
        return None

    row_data = data[table]['rows']
    column_data = data[table]['columns']

    parsed_data: defaultdict | None = defaultdict(lambda: None)

    # Skip the row entries in column 'Code'
    parsed_data['col_names'] = column_data[1:]
    parsed_data['row_entries'] = [row[1:] for row in row_data]

    parsed_data['col_len'] = len(column_data) - 1
    parsed_data['row_len'] = len(row_data)

    return parsed_data
