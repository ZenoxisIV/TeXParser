# This file contains the class that generates the paper structure of the TeX document.

class Document:
    def __init__(self, paper_type: str, font_size: int, content_type: str) -> None:
        self._paper_type = paper_type
        self._font_size = font_size
        self._content_type = content_type

    def generate_document(self) -> str:
        """Creates the document class for the document."""
        return f"\\documentclass[{self._paper_type}, {self._font_size}pt]{{{self._content_type}}}" + '\n'
    
    def import_package(self, package: str, options: list[str] | None = None) -> str:
        """Imports a package for the document."""
        return f"\\usepackage{{{package}}}" + '\n' if options is None else f"\\usepackage[{', '.join(options)}]{{{package}}}" + '\n'
    
    @staticmethod
    def begin_document() -> str:
        """Begins the document environment for the document."""
        return r"\begin{document}" + '\n'
    
    @staticmethod
    def end_document() -> str:
        """Ends the document environment for the document."""
        return r"\end{document}" + '\n'