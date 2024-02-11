# This file contains the classes for generating the tables for the paper.

class ContainerTable:
    def __init__(self) -> None:
        self.table_type = "table"

    def begin_table(self, pos: str) -> str:
        return f"\\begin{{{self.table_type}}}[{pos}]" + '\n'

    def end_table(self) -> str:
        return f"\\end{{{self.table_type}}}" + '\n'

class AdjustBox(ContainerTable): # Note: Requires the adjustbox package.
    def __init__(self) -> None:
        super().__init__()
        self.table_handler = "adjustbox"
    
    def begin_adjustbox(self, width_val: str) -> str:
        return f"\\begin{{{self.table_handler}}}{{width={width_val}}}" + '\n'
    
    def end_adjustbox(self) -> str:
        return f"\\end{{{self.table_handler}}}" + '\n'

class Tabular(AdjustBox):
    def __init__(self, sep_lines: bool = True) -> None:
        super().__init__()
        self.table_env = "tabular"
        self.sep_lines = sep_lines

