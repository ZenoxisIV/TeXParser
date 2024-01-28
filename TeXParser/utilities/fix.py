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