# This file contains the class for generating headers including titles and sections for the paper.

from utilities.format_fix import translation_table
        
class Title:
    def __init__(self, title: str) -> None:
        self._title = title

    def generate_title(self) -> str:
        formatted_title = translation_table(self._title).split('\n')
        temp = ""
        for count, line in enumerate(formatted_title, 1):
            TeX_line = r"\textsc{\large \textbf{" + line + r"}}"

            if count == len(formatted_title):
                temp += TeX_line
                continue
            
            temp += TeX_line + r"\\[0.15cm]" + '\n'

        build_title = [
            r"\begin{center}",
            temp,
            r"\end{center}",
            r"\vspace{1em}",
            '',
        ]

        return '\n'.join(build_title)
    
class Section:
    def __init__(self, section_name: str) -> None:
        self._section_name = section_name

    def generate_section(self) -> str:
        return f"\\section{{{self._section_name}}}" + '\n'
    
class Subsection(Section):
    def __init__(self, section_name: str) -> None:
        super().__init__(section_name)

    def generate_subsection(self) -> str:
        return f"\\subsection{{{self._section_name}}}" + '\n'

class Subsubsection(Subsection):
    def __init__(self, section_name: str) -> None:
        super().__init__(section_name)
    
    def generate_subsubsection(self) -> str:
        return f"\\subsubsection{{{self._section_name}}}" + '\n'

