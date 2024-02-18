# This file contains the classes for generating the tables for the paper.
from copy import deepcopy

class ContainerTable:
    def __init__(self) -> None:
        self.table_type = "table"

    def begin_table(self, pos: str) -> str:
        """Begins the table environment for the table."""
        return f"\\begin{{{self.table_type}}}[{pos}]" + '\n'

    def end_table(self) -> str:
        """Ends the table environment for the table."""
        return f"\\end{{{self.table_type}}}" + '\n'
    
    def set_arraystretch(self, stretch: float) -> str:
        """Sets the width of each cell for the table."""
        return f"\\renewcommand{{\\arraystretch}}{{{stretch}}}" + '\n'
    
    def toggle_centering(self) -> str:
        """Toggles the centering of the whole table."""
        return r"\centering" + '\n'

class AdjustBox(ContainerTable): # Note: Requires the adjustbox package.
    def __init__(self) -> None:
        super().__init__()
        self.table_handler = "adjustbox"
    
    def begin_adjustbox(self, width_val: str) -> str:
        """Begins the adjustbox environment for the table."""
        return f"\\begin{{{self.table_handler}}}{{width={width_val}}}" + '\n'
    
    def end_adjustbox(self) -> str:
        """Ends the adjustbox environment for the table."""
        return f"\\end{{{self.table_handler}}}" + '\n'

class Tabular(AdjustBox):
    def __init__(self, table_format: dict[str, str]) -> None:
        super().__init__()
        self.table_env = "tabular"
        self.table_format = table_format

    def begin_tabular(self, section_num: str) -> str:
        """Begins the tabular environment for the table."""
        return f"\\begin{{{self.table_env}}}{{{self.table_format[section_num]}}}" + '\n'
    
    def end_tabular(self) -> str:
        """Ends the tabular environment for the table."""
        return f"\\end{{{self.table_env}}}" + '\n'
    
    def generate_headers(self, headers: list[str]) -> str:
        """Generates the headers for the table."""
        build_table_headers = ""
        for i, header in enumerate(headers):
            if header == '\n':
                build_table_headers += header
                continue

            build_table_headers += header

            if i != len(headers) - 1:
                build_table_headers += " & "
        return build_table_headers
    
    def generate_entries(self, data: dict, default_fields: list[str] | None = None) -> str:
        """Generates the entries for the table."""

        required_keys = ['col_len', 'row_entries']
        if any(key not in data for key in required_keys):
            raise ValueError("Missing required key(s)")

        entries = ""
        fields = deepcopy(default_fields) if default_fields is not None else []
        prio_rows = []
        remaining_rows = deepcopy(data['row_entries'])

        for field in fields:
            for row in data['row_entries']:
                is_present = False
                if field in row:
                    prio_rows.append(remaining_rows.pop(remaining_rows.index(row)))
                    is_present = True
                    break
            if not is_present:
                prio_rows.append(tuple([field] + [None for _ in range(data['col_len'])]))

        for row in prio_rows:
            for j in range(data['col_len']):
                entries += row[j] if row[j] is not None else ''
                entries += " & "  if j != data['col_len'] - 1 else ' ' + r"\\" + ' ' + self.generate_horizontal_line()
            entries += '\n'
        
        for row in remaining_rows:
            for j in range(data['col_len']):
                entries += row[j] if row[j] is not None else ''
                entries += " & "  if j != data['col_len'] - 1 else ' ' + r"\\" + ' ' + self.generate_horizontal_line()
            entries += '\n'
                
        return entries
    
    @staticmethod
    def generate_multirow(span: int, content: str | None = None) -> str:
        """Generates merged rows for the table."""
        return f"\\multirow{{{span}}}{{*}}{{}}" if content is None else f"\\multirow{{{span}}}{{*}}{{{content}}}"
    
    @staticmethod
    def generate_multicolumn(span: int, align: str, content: str | None = None) -> str:
        """Generates merged columns for the table."""
        return f"\\multicolumn{{{span}}}{{{align}}}{{}}" if content is None else f"\\multicolumn{{{span}}}{{{align}}}{{{content}}}"
    
    @staticmethod
    def generate_cline(start: int, end: int) -> str:
        """Generates a horizontal line that spans the specified columns."""
        return f"\\cline{{{start}-{end}}}"
    
    @staticmethod
    def generate_horizontal_line() -> str:
        """Generates a horizontal line for the table."""
        return r"\hline"