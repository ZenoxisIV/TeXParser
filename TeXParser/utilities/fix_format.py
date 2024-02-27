# This file contains functions that are used to fix formatting issues in LaTeX code.
class OverrideFormat:
    def __init__(self, file: str | None = None) -> None:
        if file is None:
            self.tex = ""
        else:
            fd = open(file, "r")
            self.tex = fd.read()
            fd.close()

    def include_tex(self) -> str:
        """Includes the LaTeX code in the document."""
        return self.tex

    def change_titleformat(self, font_size: int, section: str, param: str) -> str:
        """Changes the title format for the document."""
        match section.lower():
            case "section":
                return generate_sectionformat(font_size, 1, param)
            case "subsection":
                return generate_sectionformat(font_size, 2, param)
            case "subsubsection":
                return generate_sectionformat(font_size, 3, param)
            case _:
                raise ValueError(f"Invalid section '{section}'.")
            
    def change_fontsize(self, size: str) -> str:
        """Changes the font size for the document."""
        return f"\\{size}"

    @staticmethod
    def begingroup() -> str:
        """Begins a group."""
        return r"\begingroup" + '\n'
    
    @staticmethod
    def endgroup() -> str:
        """Ends a group."""
        return r"\endgroup" + '\n'

def translation_table(text) -> str:
    """Translates the text to LaTeX format."""
    table = str.maketrans({'%': r"\%",
                        '$': r"\$",
                        '&': r"\&",
                        '#': r"\#",
                        '_': r"\_",
                        '{': r"\{",
                        '}': r"\}",
                        '~': r"\textasciitilde",
                        '^': r"\textasciicircum",
                        '\\': r"\textbackslash"})
    
    return text.translate(table)

def get_column_count(table_format: str) -> int:
    """Gets the number of columns in the table."""
    return table_format.count('c') + table_format.count('l') + table_format.count('r')

def generate_sectionformat(font_size: int, option: int | None = None, mode: str | None = None) -> str:
    """Generates the section format for the document."""
    section_types = [
        r"\section",           # OPTION 1
        r"\subsection",        # OPTION 2
        r"\subsubsection",     # OPTION 3
    ]

    section_types = section_types if option is None else [section_types[option - 1]]
    
    build_titleformat = ""
    for section_type in section_types:
        build_titleformat += r"\titleformat"
        build_titleformat += f"{{{section_type}}}\n" if mode is None else f"{{{section_type}}}[{mode}]\n"
        build_titleformat += f"{{\\normalfont\\fontsize{{{font_size}}}{{15}}\\bfseries}}"
        build_titleformat += f"{{{section_type[0] + 'the' + section_type[1:]}}}{{1em}}{{}}\n"

    return build_titleformat

def toggle_noindent() -> str:
    """Toggles the no indent on line for the document."""
    return r"\noindent" + '\n'

def force_linebreak() -> str:
    """Forces a line break in the document."""
    return r"\hfill" + r"\break"

def generate_fancystyle() -> str: # Note: Requires the fancyhdr package
    """Generates the fancy style for the document."""
    return r"\pagestyle{fancy}" + '\n'

# === WARNING: DO NOT USE THE FOLLOWING WITHOUT generate_fancystyle() ===

def clear_fancyhf() -> str:
    """Clears the fancy header and footer."""
    return r"\fancyhf{}" + '\n'

def set_headerrule(width: int) -> str:
    """Sets the width of the header rule."""
    return f"\\renewcommand{{\\headrulewidth}}{{{width}pt}}" + '\n'

def set_fancyfooter(location: list[str], content: str) -> str:
    """Sets the fancy footer for the document."""
    return f"\\fancyfoot[{', '.join(location)}]{{{content}}}" + '\n'

def set_fancyheader(location: list[str], content: str) -> str:
    """Sets the fancy header for the document."""
    return f"\\fancyhead[{', '.join(location)}]{{{content}}}" + '\n'

# =======================================================================