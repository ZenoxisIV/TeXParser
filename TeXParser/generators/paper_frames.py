# This file contains the class for generating the frame environments for the paper

class MDFrame: # Note: Requires the mdframed package.
    def __init__(self, content: list[str]) -> None:
        self._content = content

    def generate_mdframe(self) -> str:
        build_frame = [
            r"\begin{quote}",
            r"\begin{mdframed}",
            r"{\fontfamily{cmss}\selectfont",
            "\n".join(self._content),
            r"}",
            r"\end{mdframed}",
            r"\end{quote}"
        ]

        return '\n'.join(build_frame)