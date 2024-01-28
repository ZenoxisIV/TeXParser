def generate_fancyheader() -> str:
    return r"""
\pagestyle{fancy}
\fancyhf{} % sets both header and footer to nothing
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[R]{%
\small\emph{Page \thepage\ of \pageref{LastPage}}\hspace{15pt}%
}
"""

def generate_hypersetup(link_color: str, cite_color: str, url_color: str) -> str:
    temp = [r"\hypersetup{",
            r"colorlinks,",
            f"linkcolor={{{link_color}}},",
            f"citecolor={{{cite_color}}},",
            f"urlcolor={{{url_color}}}",
            r"}",
    ]
    return '\n'.join(temp)

def generate_newcommands() -> str:
    return '\n' + r"\newcommand\tab[1][0.30cm]{\hspace*{#1}}"