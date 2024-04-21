# This file contains the class for generating the lists for the paper.

from re import match

class Bullet:
    def __init__(self, block_text: dict[str, str]) -> None:
        self._block_text = block_text
        self.bullet_type = "itemize"

    def generate_bullets(self) -> str:
        """Creates the bullet points for the document."""
        def is_b_string(s: str):
            pattern = r'^b\d$' # Matches strings like 'b1', 'b2', ...
            return bool(match(pattern, s))

        temp = ""

        for key, value in self._block_text.items():
            if is_b_string(key):
                temp += r"\item " + value + '\n'

        return temp

    def begin_bullet(self, indent_offset: str | None = None) -> str:
        """Begins the bullet environment for the document."""
        return f"\\begin{{{self.bullet_type}}}" + '\n' if indent_offset is None else f"\\begin{{{self.bullet_type}}}[left={indent_offset}]" + '\n'
    
    def end_bullet(self) -> str:
        """Ends the bullet environment for the document."""
        return f"\\end{{{self.bullet_type}}}" + '\n'

class Ordered(Bullet): # Note: Requires the enumitem package.
    def __init__(self, block_text: dict[str, str]) -> None:
        super().__init__(block_text)
        self.bullet_type = "enumerate"