# This file contains functions that manages and generates some important styles for the TeX file.

from typing import Callable

def generate_hypersetup(link_color: str, cite_color: str, url_color: str) -> str: # Warning: Requires the xcolor package
    """Generates the hypersetup (i.e., color of document links, citations, URLs) for the document."""
    temp = [r"\hypersetup{",
            r"colorlinks,",
            f"linkcolor={{{link_color}}},",
            f"citecolor={{{cite_color}}},",
            f"urlcolor={{{url_color}}}",
            r"}",
    ]
    return '\n'.join(temp)

def generate_footnote_mark(symbol: str) -> str:
    """Generates a footnote mark for the document."""
    return f"\\footnotemark[{symbol}]"

def generate_footnote_text(symbol: str, content: dict[str, str]) -> str:
    """Generates the footnote text which corresponds to a footnote mark for the document."""
    return f"\\footnotetext[{symbol}]{{{content[symbol]}}}" + '\n'

def bold_text(text: str) -> str:
    """Bolds the text."""
    return f"\\textbf{{{text}}}"

def italic_text(text: str) -> str:
    """Italicizes the text."""
    return f"\\textit{{{text}}}"

def hyperlink_text(link: str) -> str:
    """Creates a hyperlink for the text."""
    return f"\\href{{{link}}}{{{link}}}"

def modify_substring(paragraph: str, substring: str, func: Callable[[str], str]) -> str:
    """Modifies a substring in a paragraph using a function."""
    return paragraph.replace(substring, func(substring))