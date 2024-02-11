# This file contains functions that are used to fix formatting issues in LaTeX code.

def translation_table(text) -> str:
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

def generate_titleformat(font_size: int) -> str:
    section_types = [
        r"\section",
        r"\subsection",
        r"\subsubsection",
    ]
    
    build_titleformat = ""
    for section_type in section_types:
        build_titleformat += r"\titleformat"
        build_titleformat += f"{{{section_type}}}\n"
        build_titleformat += f"{{\\normalfont\\fontsize{{{font_size}}}{{15}}\\bfseries}}"
        build_titleformat += f"{{{section_type[0] + "the" + section_type[1:]}}}{{1em}}{{}}\n"

    return build_titleformat

def generate_fancystyle() -> str: # Note: Requires the fancyhdr package
    return r"\pagestyle{fancy}" + '\n'

# === WARNING: DO NOT USE THE FOLLOWING WITHOUT generate_fancystyle() ===

def clear_fancyhf() -> str:
    return r"\fancyhf{}" + '\n'

def set_headerrule(width: int) -> str:
    return f"\\renewcommand{{\\headrulewidth}}{{{width}pt}}" + '\n'

def set_fancyfooter(location: list[str], content: str) -> str:
    return f"\\fancyfoot[{', '.join(location)}]{{{content}}}" + '\n'

def set_fancyheader(location: list[str], content: str) -> str:
    return f"\\fancyhead[{', '.join(location)}]{{{content}}}" + '\n'

# =======================================================================