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

def build_titleformat() -> str:
    return r"""
\titleformat{\section}
{\normalfont\fontsize{10}{15}\bfseries}{\thesection}{1em}{}

\titleformat{\subsection}
{\normalfont\fontsize{10}{15}\bfseries}{\thesubsection}{1em}{}

\titleformat{\subsubsection}
{\normalfont\fontsize{10}{15}\bfseries}{\thesubsubsection}{1em}{}
"""

def build_fancyheader() -> str:
    return r"""
\pagestyle{fancy}
\fancyhf{} % sets both header and footer to nothing
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[R]{%
\small\emph{Page \thepage\ of \pageref{LastPage}}\hspace{15pt}%
}
"""

def build_hypersetup() -> str:
    return r"""
\hypersetup{
    colorlinks,
    linkcolor={black},
    citecolor={black},
    urlcolor={black}
}
"""

def build_newcommands() -> str:
    return r"""
\newcommand\tab[1][0.30cm]{\hspace*{#1}}
"""

class Document:
    def __init__(self, paper_type: str, font_size: int, content_type: str) -> None:
        self.paper_type = paper_type
        self.font_size = font_size
        self.content_type = content_type

    def generate_document(self) -> str:
        return f"\\documentclass[{self.paper_type}, {self.font_size}pt]{{{self.content_type}}}"
    
    def import_package(self, package: str, options: list[str] | None = None) -> str:
        return f"\\usepackage{{{package}}}" if options is None else f"\\usepackage[{', '.join(options)}]{{{package}}}"
    
    def begin_document(self) -> str:
        return r"\begin{document}"
    
    def end_document(self) -> str:
        return r"\end{document}"
    
class Title:
    def __init__(self, title: str) -> None:
        self.title = title

    def generate_title(self) -> str:
        new_title = translation_table(self.title)

        if len(new_title) > 50:
            temp = r"\textsc{\large \textbf{"
            temp += new_title[:49] + r"}}" + r"\\[0.15cm]" + "\n" 
            temp += r"\textsc{\large \textbf{"
            temp += new_title[50:] + r"}}"
        else:
            temp = r"\textsc{\large \textbf{" + self.title + r"}}"

        build_title = [
            r"\begin{center}",
            temp,
            r"\end{center}",
            r"\vspace{1em}",
        ]

        return '\n'.join(build_title)

class MDFrame:
    def __init__(self, agency_name: (str), respondent: (str), 
                 position: (str), division: (str), telephone: (str), 
                 repondent_email: (str)) -> None:
        self.agency_name = agency_name
        self.respondent = respondent
        self.position = position
        self.division = division
        self.telephone = telephone
        self.respondent_email = repondent_email

        self.content = [
            r"AGENCY NAME: (NO CONTENT [1]) University of the Philippines Diliman (NO CONTENT [2])",
            r"Respondent (IS Planner/CIO/MIS Head)\footnotemark[1]: (NO CONTENT) Dr. Manuel C. Ramos, Jr. (NO CONTENT [2])",
            r"Position/D\'esignation: (NO CONTENT [1]) Director (NO CONTENT [2])",
            r"Division/Section/Unit: (NO CONTENT [1]) University Computer Center (NO CONTENT [2])",
            r"Telephone/Fax Number: (NO CONTENT [1]) 8981-8500 local 2050 (NO CONTENT [2])",
            r"Respondent's Email Address: (NO CONTENT [1])",
        ]

    def generate_mdframe(self) -> str:
        full_agency = self.content[0].replace("(NO CONTENT [1])", self.agency_name[0]).replace("(NO CONTENT [2])", self.agency_name[1])
        full_respondent = self.content[1].replace("(NO CONTENT)", self.respondent[0]).replace("(NO CONTENT [2])", self.respondent[1])
        full_position = self.content[2].replace("(NO CONTENT [1])", self.position[0]).replace("(NO CONTENT [2])", self.position[1])
        full_division = self.content[3].replace("(NO CONTENT [1])", self.division[0]).replace("(NO CONTENT [2])", self.division[1])
        full_telephone = self.content[4].replace("(NO CONTENT [1])", self.telephone[0]).replace("(NO CONTENT [2])", self.telephone[1])
        full_respondent_email = self.content[5].replace("(NO CONTENT [1])", self.respondent_email[0]).replace("(NO CONTENT [2])", self.respondent_email[1])

        build_frame = [
            r"\begin{quote}",
            r"\begin{mdframed}",
            r"{\fontfamily{cmss}\selectfont",
            full_agency,
            full_respondent,
            full_position,
            full_division,
            full_telephone,
            full_respondent_email,
            r"}",
            r"\end{mdframed}",
            r"\end{quote}"
        ]

        return '\n'.join(build_frame)

if __name__ == "__main__":
    doc = Document("a4paper", 10, "article")
    title = Title("ANNEX A-5: EXISTING INFORMATION & COMMUNICATIONS TECHNOLOGY (ICT) INFRASTRUCTURE INVENTORY")
    mdframe = None

    build_TeX = [
        doc.generate_document(),
        title.generate_title(),
        build_titleformat(),
        build_hypersetup(),
        build_newcommands(),
        build_fancyheader(),
    ]

    print(''.join(build_TeX))