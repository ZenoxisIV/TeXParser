from generators.paper_tables import Tabular
from utilities.style_fix import make_tickbox

class Questionnaire:
    def __init__(self, data: dict, format: dict[str, str], options: list[str] | None = None) -> None:
        self.data = data
        self.format = format
        self.options = options
        self.table = Tabular(self.format)

    def generate_options_inline(self, questions: list[str], q_start_idx: int = 0, q_end_idx: int = 99, start_col_search: str | None = None) -> str:
        """Generates the questionnaire with options inline with the question."""
        get_key = list(self.format.keys())[0]

        def generate_items(self) -> str:
            """Generates the items for the questionnaire."""
            target_idx = self.data['col_names'].index(start_col_search)
            entries = self.data['row_entries'][0][target_idx:]
            count = 0
            print(entries)
            build_ques = ""
            for i, question in enumerate(questions[q_start_idx: q_end_idx + 1], start=q_start_idx + 1):
                build_ques += f"\\footnotesize {get_key}.{i} & \\footnotesize {question} & "
                flip = True
                for j, res in enumerate(self.options):

                    if entries[count] is None:
                        build_ques += make_tickbox(name=res)
                    elif res.upper() == "YES" or res.upper() == "NO":
                        build_ques += make_tickbox(bool(int(entries[count])) == flip, name=res)
                        flip = not flip
                    else:
                        build_ques += make_tickbox(True, name=res) if entries[count] == res else make_tickbox(name=res)

                    if j != len(self.options) - 1:
                        build_ques += " & "
                build_ques += r" \\ " + '\n'
                count += 1
        
            return build_ques
        
        if self.options is None:
            raise ValueError("Options not found.")
        
        if start_col_search is None:
            raise ValueError("Column to search not found.")

        build_ques = ''.join([self.table.begin_table("H"),
                              self.table.begin_adjustbox(r"\textwidth"),
                              self.table.begin_tabular(get_key),

                              generate_items(self),

                              self.table.end_tabular(),
                              self.table.end_adjustbox(),
                              self.table.end_table()
                              ])

        return build_ques
    
    def generate_fill_blank(self, questions: list[str], q_start_idx: int = 0, q_end_idx: int = 99, start_col_search: str | None = None) -> str:
        """Generates the questionnaire with fill-in-the-blank answers."""
        get_key = list(self.format.keys())[0]

        def generate_items(self) -> str:
            target_idx = self.data['col_names'].index(start_col_search)
            entries = self.data['row_entries'][0][target_idx:]
            count = q_start_idx + 1
            build_ques = ""
            for i, question in enumerate(questions[q_start_idx: q_end_idx + 1]):
                build_ques += f"\\footnotesize {get_key}.{count} & \\footnotesize {question} "
                build_ques += f"\\footnotesize \\textbf{{{entries[i] if entries[i] is not None else ''}}}"
                build_ques += r" \\ " + '\n'
                count += 1

            return build_ques
        
        if start_col_search is None:
            raise ValueError("Column to search not found.")
        
        build_ques = ''.join([self.table.begin_table("H"),
                              self.table.begin_adjustbox(r"\textwidth"),
                              self.table.begin_tabular(get_key),

                              generate_items(self),

                              self.table.end_tabular(),
                              self.table.end_adjustbox(),
                              self.table.end_table()
                              ])
        
        return build_ques



