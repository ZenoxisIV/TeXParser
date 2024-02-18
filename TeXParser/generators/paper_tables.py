# This file contains the classes for generating the tables for the paper.

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
    def __init__(self) -> None:
        super().__init__()
        self.table_env = "tabular"

    def begin_tabular(self, col_format: str) -> str:
        """Begins the tabular environment for the table."""
        return f"\\begin{{{self.table_env}}}{{{col_format}}}" + '\n'
    
    def end_tabular(self) -> str:
        """Ends the tabular environment for the table."""
        return f"\\end{{{self.table_env}}}" + '\n'
    
    def generate_entries(self, data: dict, default_fields: list[str] | None = None) -> str:
        """Generates the entries for the table."""
        for required_key in ['row_len', 'col_len', 'row_entries']:
            if required_key not in data:
                raise ValueError(f"Missing required key: '{required_key}'")
        
        entries = ""
        if default_fields is None:
            for i in range(data['row_len'] - 1):
                for j in range(data['col_len'] - 1):
                    if j+1 != data['col_len'] - 1:
                        entries += f"{data['row_entries'][i][j+1] if data['row_entries'][i][j+1] is not None else ''}" + " & "
                    else:
                        entries += f"{data['row_entries'][i][j+1] if data['row_entries'][i][j+1] is not None else ''}" + r"\\" \
                                    + ' ' + self.generate_horizontal_line()
                entries += '\n'
        else:
            ...
        
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