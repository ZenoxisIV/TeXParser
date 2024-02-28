# This file handles errors that may occur during the execution of the program.

import logging
from os import makedirs
from typing import Any, Type
from handle.warnings import ClassWarnings
from inspect import stack

# Configure logging settings
log_directory = './TeXParser/handle/logs/'  # Specify the log directory here
log_filename = 'parse_errors.log'  # Specify the log filename here
log_filepath = f'{log_directory}/{log_filename}'

# Create the log directory if it doesn't exist
makedirs(log_directory, exist_ok=True)

logging.basicConfig(filename=log_filepath, level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

def checkNoneorEmpty(value: Any, issue: Type[UserWarning]) -> bool:
    if value is None or len(value) <= 0:
        process_name = stack()[1].function
        file_name = stack()[1].filename
        line_number = stack()[1].lineno
        warning_message = f"File '{file_name}', in line {line_number}, in function {process_name}(): The value is of NoneType or empty."
        logging.warning(warning_message)
        ClassWarnings.alert(ClassWarnings(issue), warning_message)
        return True
    
    return False

def checkTable(data: dict[str, Any], table: str, issue: Type[UserWarning]) -> bool:
    if table not in data:
        process_name = stack()[1].function
        file_name = stack()[1].filename
        line_number = stack()[1].lineno
        warning_message = f"File '{file_name}', in line {line_number}, in function {process_name}(): Table '{table}' not found in the JSON data."
        logging.warning(warning_message)
        ClassWarnings.alert(ClassWarnings(issue), warning_message)
        return True
    
    return False