# This file contains the class that generates the paper structure of the TeX document.

class Document:
    def __init__(self, paper_type: str, font_size: int, content_type: str) -> None:
        self._paper_type = paper_type
        self._font_size = font_size
        self._content_type = content_type

    def generate_document(self) -> str:
        return f"\\documentclass[{self._paper_type}, {self._font_size}pt]{{{self._content_type}}}" + '\n'
    
    def import_package(self, package: str, options: list[str] | None = None) -> str:
        return f"\\usepackage{{{package}}}" + '\n' if options is None else f"\\usepackage[{', '.join(options)}]{{{package}}}" + '\n'
    
    @staticmethod
    def generate_footnote_mark(symbol: str) -> str:
        return f"\\footnotemark[{symbol}]"

    @staticmethod
    def generate_footnote_text(symbol: str, content: str) -> str:
        return f"\\footnotetext[{symbol}]{{{content}}}" + '\n'
    
    @staticmethod
    def begin_document() -> str:
        return r"\begin{document}" + '\n'
    
    @staticmethod
    def end_document() -> str:
        return r"\end{document}" + '\n'