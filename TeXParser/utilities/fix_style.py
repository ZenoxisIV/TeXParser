# This file contains functions that manages and generates some important styles for the TeX file.

from typing import Callable

def process_text(sentences: list[str]) -> str:
    """Processes the text in a list line-by-line for the document."""
    s = ' '+ r"\\" + '\n'
    return s.join(sentences) + '\n'

def generate_section(section_name: str) -> str:
    """Create a section for the document."""
    return f"\\section{{{section_name}}}" + '\n'

def generate_subsection(section_name: str) -> str:
    """Create a subsection for the document."""
    return f"\\subsection{{{section_name}}}" + '\n'

def generate_subsubsection(section_name: str) -> str:
    """Create a subsubsection for the document."""
    return f"\\subsubsection{{{section_name}}}" + '\n'

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

def make_tickbox(is_ticked: bool = False, name: str | None = None) -> str:
    """Creates a tickbox for the document."""
    tickbox = r"\Large$\boxtimes$" if is_ticked else r"\Large$\square$"
    return tickbox if name is None else f"{tickbox} \\footnotesize {name}"

def generate_footnote_mark(symbol: str, is_protected = False) -> str:
    """Generates a footnote mark for the document."""
    return f"\\protect\\footnotemark[{symbol}]" if is_protected else f"\\footnotemark[{symbol}]"

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

def append_footnotemark(text: str, symbol: str, is_protected = False) -> str:
    """Appends a footnote mark to the text."""
    build_string = text

    if is_protected:
        build_string += r"\protect"

    build_string += f"\\footnotemark[{symbol}]"
    return build_string


def modify_substring(paragraph: str, substring: str, func: Callable, symbol: str | None = None, flag = False) -> str:
    """Modifies a substring in a paragraph using a function."""
    return paragraph.replace(substring, func(substring)) if symbol is None else paragraph.replace(substring, func(substring, symbol, flag))

def newpage() -> str:
    """Creates a new page."""
    return '\n' + r"\newpage" + '\n' * 2

def vertical_space(space: str) -> str:
    """Creates a vertical space."""
    return '\n' + f"\\vspace{{{space}}}" + '\n' * 2
