# This file contains functions that manages and generates some important styles for the TeX file.

from typing import Callable

def generate_hypersetup(link_color: str, cite_color: str, url_color: str) -> str: # Warning: Requires the xcolor package
    temp = [r"\hypersetup{",
            r"colorlinks,",
            f"linkcolor={{{link_color}}},",
            f"citecolor={{{cite_color}}},",
            f"urlcolor={{{url_color}}}",
            r"}",
    ]
    return '\n'.join(temp)

def generate_footnote_mark(symbol: str) -> str:
    return f"\\footnotemark[{symbol}]"

def generate_footnote_text(symbol: str, content: dict[str, str]) -> str:
    return f"\\footnotetext[{symbol}]{{{content[symbol]}}}" + '\n'

def bold_text(text: str) -> str:
    return f"\\textbf{{{text}}}"

def italic_text(text: str) -> str:
    return f"\\textit{{{text}}}"

def hyperlink_text(link: str) -> str:
    return f"\\href{{{link}}}{{{link}}}"

def modify_substring(paragraph: str, substring: str, func: Callable[[str], str]) -> str:
    return paragraph.replace(substring, func(substring))