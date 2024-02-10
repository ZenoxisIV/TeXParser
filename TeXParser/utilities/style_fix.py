# This file contains functions that manages and generates some important styles for the TeX file.
from typing import Callable

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

def generate_hypersetup(link_color: str, cite_color: str, url_color: str) -> str: # Warning: Requires the xcolor package
    temp = [r"\hypersetup{",
            r"colorlinks,",
            f"linkcolor={{{link_color}}},",
            f"citecolor={{{cite_color}}},",
            f"urlcolor={{{url_color}}}",
            r"}",
    ]
    return '\n'.join(temp)

def generate_newcommand_TAB() -> str:
    return r"\newcommand\tab[1][0.30cm]{\hspace*{#1}}"

def bold_text(text: str) -> str:
    return f"\\textbf{{{text}}}"

def italic_text(text: str) -> str:
    return f"\\textit{{{text}}}"

def modify_substring(paragraph: str, substring: str, func: Callable[[str], str]) -> str:
    return paragraph.replace(substring, func(substring))