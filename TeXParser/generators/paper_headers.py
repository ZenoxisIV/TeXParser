# This file contains the class for generating headers including titles and sections for the paper.

from utilities.format_fix import translation_table
        
class Title:
    def __init__(self, title: str) -> None:
        self._title = title

    def generate_title(self) -> str:
        new_title = translation_table(self._title)

        if len(new_title) > 50:
            temp = r"\textsc{\large \textbf{"
            temp += new_title[:49] + r"}}" + r"\\[0.15cm]" + "\n" 
            temp += r"\textsc{\large \textbf{"
            temp += new_title[50:] + r"}}"
        else:
            temp = r"\textsc{\large \textbf{" + self._title + r"}}"

        build_title = [
            r"\begin{center}",
            temp,
            r"\end{center}",
            r"\vspace{1em}",
            '',
        ]

        return '\n'.join(build_title)
    
    def generate_titleformat(self, font_size: int) -> str:
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

