# This file contains the class for generating the frame environments for the paper

from utilities.format_fix import translation_table

class MDFrame:
    def __init__(self, content: list[str]) -> None:
        self.content = content

    def generate_mdframe(self) -> str:
        build_frame = [
            r"\begin{quote}",
            r"\begin{mdframed}",
            r"{\fontfamily{cmss}\selectfont",
            "\n".join(self.content),
            r"}",
            r"\end{mdframed}",
            r"\end{quote}"
        ]

        return '\n'.join(build_frame)