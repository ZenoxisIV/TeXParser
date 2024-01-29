# This file contains the class that generates the paper structure of the TeX document.

class Document:
    def __init__(self, paper_type: str, font_size: int, content_type: str) -> None:
        self.paper_type = paper_type
        self.font_size = font_size
        self.content_type = content_type

    def generate_document(self) -> str:
        return f"\\documentclass[{self.paper_type}, {self.font_size}pt]{{{self.content_type}}}" + '\n'
    
    def import_package(self, package: str, options: list[str] | None = None) -> str:
        return f"\\usepackage{{{package}}}" + '\n' if options is None else f"\\usepackage[{', '.join(options)}]{{{package}}}" + '\n'
    
    def begin_document(self) -> str:
        return r"\begin{document}" + '\n'
    
    def end_document(self) -> str:
        return r"\end{document}" + '\n'