# This file contains the classes for generating the tables for the paper.

from typing import Any
from copy import deepcopy
from utilities.fix_style import make_tickbox, newpage, begin_center, end_center, bold_text
from utilities.fix_format import getColumnCount
from handle.warnings import NoDataFoundWarning
from handle.checker import checkNoneorEmpty

class ContainerTable:
    def __init__(self) -> None:
        self.table_type = "table"
        self.pos: str | None = None
        self.stretch: float | None = None

    def begin_table(self, pos: str) -> str:
        """Begins the table environment for the table."""
        self.pos = pos
        return f"\\begin{{{self.table_type}}}[{pos}]" + '\n'

    def end_table(self) -> str:
        """Ends the table environment for the table."""
        return f"\\end{{{self.table_type}}}" + '\n'
    
    def set_arraystretch(self, stretch: float) -> str:
        """Sets the width of each cell for the table."""
        self.stretch = stretch
        return f"\\renewcommand{{\\arraystretch}}{{{stretch}}}" + '\n'
    
    def toggle_centering(self) -> str:
        """Toggles the centering of the whole table."""
        return r"\centering" + '\n'

class AdjustBox(ContainerTable): # Note: Requires the adjustbox package.
    def __init__(self) -> None:
        super().__init__()
        self.table_handler = "adjustbox"
        self.width_val: str | None = None
    
    def begin_adjustbox(self, width_val: str) -> str:
        """Begins the adjustbox environment for the table."""
        self.width_val = width_val
        return f"\\begin{{{self.table_handler}}}{{width={width_val}}}" + '\n'
    
    def end_adjustbox(self) -> str:
        """Ends the adjustbox environment for the table."""
        return f"\\end{{{self.table_handler}}}" + '\n'

class Tabular(AdjustBox):
    def __init__(self, table_format: dict[str, str]) -> None:
        super().__init__()
        self.table_env = "tabular"
        self.table_format = table_format
        self.section_num: str | None = None
        self.header_set: str | None = None

    def begin_tabular(self, section_num: str, parameter: str | None = None) -> str:
        """Begins the tabular environment for the table."""
        # SPECIAL ENVIRONMENT:
        # The @{}c@{} specifies that the column should be centered with no space on either side.
        if section_num == "@{}c@{}":
            table_format = section_num
        else:
            try:
                table_format = self.table_format[section_num]
            except KeyError:
                raise KeyError(f"Table format not found for section number: {section_num}")
        
        self.section_num = section_num
        return f"\\begin{{{self.table_env}}}{{{table_format}}}" + '\n' if parameter is None else f"\\begin{{{self.table_env}}}[{parameter}]{{{section_num}}}" + '\n'
    
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
        self.header_set = build_table_headers
        return build_table_headers
    
    def generate_entries(self, data: dict[str, Any] | None, default_fields: list[str] | None = None, limit: int = 30, reset_limit: int = 30, tickbox_cols: list[str] | None = None) -> str:
        """Generates the entries for the table."""
        def premature_end_table(self) -> str:
            """Ends the table environment prematurely."""
            return self.end_tabular() + self.end_adjustbox() + self.end_table()
        
        def spawn_new_table(self) -> str:
            """Spawns a new table environment."""
            return self.begin_table(self.pos) + self.set_arraystretch(self.stretch) + self.toggle_centering() + self.begin_adjustbox(self.width_val) + self.begin_tabular(self.section_num) + self.generate_horizontal_line()
        
        def regen_headers(self) -> str:
            """Regenerates the headers for the table."""
            return self.header_set + '\n'
        
        if checkNoneorEmpty(data, NoDataFoundWarning) or checkNoneorEmpty(data['col_names'], NoDataFoundWarning):
            count = getColumnCount(self.table_format[self.section_num])
            return f"\\multicolumn{{{count}}}{{|c|}}{{\\textbf{{* NO DATA FOUND *}}}}" + r" \\ " + r"\hline"
        
        required_keys = ['col_len', 'col_names', 'row_entries']
        missing_keys = [key for key in required_keys if key not in data]
        if missing_keys:
            raise ValueError(f"Required key(s) not found in the data: {', '.join(missing_keys)}")
        
        if tickbox_cols is not None:
            missing_cols = [col for col in tickbox_cols if col not in data['col_names']]
            if missing_cols:
                raise ValueError(f"Column(s) not found for boolean entries: {', '.join(missing_cols)}")
            
            for idx, col in enumerate(data['col_names']):
                if col in tickbox_cols:
                    for i in range(data['row_len']):
                        data['row_entries'][i][idx] = make_tickbox(bool(int(data['row_entries'][i][idx])))

        entries = ""
        fields = deepcopy(default_fields) if default_fields is not None else []
        prio_rows = []
        remaining_rows = deepcopy(data['row_entries'])

        is_present = None
        for field in fields:
            for row in data['row_entries']:
                is_present = False
                if field in row:
                    prio_rows.append(remaining_rows.pop(remaining_rows.index(row)))
                    is_present = True
                    break
            if not is_present:
                prio_rows.append(tuple([field] + [None for _ in range(data['col_len'])]))
        
        row_track = 0
        for row in prio_rows:
            for j in range(data['col_len']):
                entries += row[j] if row[j] is not None else ''
                entries += " & "  if j != data['col_len'] - 1 else r" \\ " + self.generate_horizontal_line()
            entries += '\n'
            row_track += 1

            # If limit is reached, we output the next entries of the table in a new page
            if row_track == limit:
                entries += premature_end_table(self) + newpage() + spawn_new_table(self) + regen_headers(self)
                row_track = 0
    
        for row in remaining_rows:
            for j in range(data['col_len']):
                entries += row[j] if row[j] is not None else ''
                entries += " & "  if j != data['col_len'] - 1 else r" \\ " + self.generate_horizontal_line()
            entries += '\n'
            row_track += 1

            if row_track == limit:
                entries += premature_end_table(self) + newpage() + spawn_new_table(self) + regen_headers(self)
                row_track = 0
                limit = reset_limit
                
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