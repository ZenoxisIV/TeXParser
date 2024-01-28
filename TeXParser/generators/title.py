from utilities.fix import translation_table
        
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
            build_titleformat += f"{{{section_type}}}{{1em}}{{}}\n"

        return build_titleformat