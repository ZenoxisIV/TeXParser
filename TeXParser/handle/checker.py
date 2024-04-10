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

logging.basicConfig(filename=log_filepath, level=logging.INFO, format='[%(asctime)s] [%(levelname)s] [%(name)s/%(module)s]: %(message)s')

def check_none_or_empty(value: Any, issue: Type[UserWarning]) -> bool:
    if value is None or len(value) <= 0:
        process_name = stack()[1].function
        file_name = stack()[1].filename
        line_number = stack()[1].lineno
        warning_message = f"File '{file_name}', in line {line_number}, in function {process_name}(): The value is of NoneType or empty."
        logging.warning(warning_message)
        ClassWarnings.alert(ClassWarnings(issue), warning_message)
        return True
    
    return False

def check_table(data: dict[str, Any], table: str, issue: Type[UserWarning]) -> bool:
    if table not in data:
        process_name = stack()[1].function
        file_name = stack()[1].filename
        line_number = stack()[1].lineno
        warning_message = f"File '{file_name}', in line {line_number}, in function {process_name}(): Table '{table}' not found in the JSON data."
        logging.warning(warning_message)
        ClassWarnings.alert(ClassWarnings(issue), warning_message)
        return True
    
    return False

def raise_instance_error(message: str) -> None:
    process_name = stack()[1].function
    file_name = stack()[1].filename
    line_number = stack()[1].lineno
    error_message = f"File '{file_name}', in line {line_number}, in function {process_name}(): {message}"
    logging.error(error_message)
    raise ValueError(error_message)

def raise_table_format_error(section_num: str) -> None:
    process_name = stack()[1].function
    file_name = stack()[1].filename
    line_number = stack()[1].lineno
    error_message = f"File '{file_name}', in line {line_number}, in function {process_name}(): Table format not found for section number: {section_num}"
    logging.error(error_message)
    raise KeyError(error_message)

def raise_missing_keys_error(message: str, missing_keys: list[str]) -> None:
    process_name = stack()[1].function
    file_name = stack()[1].filename
    line_number = stack()[1].lineno
    error_message = f"File '{file_name}', in line {line_number}, in function {process_name}(): {message}: {', '.join(missing_keys)}"
    logging.error(error_message)
    raise KeyError(error_message)

def raise_missing_columns_error(message: str, missing_cols: list[str]) -> None:
    process_name = stack()[1].function
    file_name = stack()[1].filename
    line_number = stack()[1].lineno
    error_message = f"File '{file_name}', in line {line_number}, in function {process_name}(): {message}: {', '.join(missing_cols)}"
    logging.error(error_message)
    raise ValueError(error_message)

def raise_missing_options_error() -> None:
    process_name = stack()[1].function
    file_name = stack()[1].filename
    line_number = stack()[1].lineno
    error_message = f"File '{file_name}', in line {line_number}, in function {process_name}(): Options not found."
    logging.error(error_message)
    raise ValueError(error_message)

def raise_column_search_error() -> None:
    process_name = stack()[1].function
    file_name = stack()[1].filename
    line_number = stack()[1].lineno
    error_message = f"File '{file_name}', in line {line_number}, in function {process_name}(): Column to search not found."
    logging.error(error_message)
    raise ValueError(error_message)