# This file contains the class for generating the questionnaire for the paper.

from generators.paper_tables import Tabular
from utilities.fix_style import make_tickbox, vertical_space
from typing import Any
from handle.warnings import ClassWarnings, NoDataFoundWarning, NoQuestionsFoundWarning

class Questionnaire:
    def __init__(self, data: dict[str, Any] | None, format: dict[str, str], options: list[str] | dict[str, dict[str, Any]] | None = None) -> None:
        self.data = data
        self.format = format
        self.options = options
        self.table = Tabular(self.format)

    def generate_options_inline(self, questions: list[str], q_start_idx: int = 0, q_end_idx: int = 99, start_col_search: str | None = None) -> str:
        """Generates the questionnaire with options inline with the question. Can process multiple inline questions in succession."""
        if self.data is None:
            ClassWarnings.alert(ClassWarnings(NoDataFoundWarning), "Data not found. Cannot generate options for the questionnaire.")
            return ""
        
        if questions is None:
            ClassWarnings.alert(ClassWarnings(NoQuestionsFoundWarning), "Questions not found. Cannot generate the questionnaire.")
            return ""
       
        get_key = list(self.format.keys())[0]

        def generate_items(self) -> str:
            """Generates the items for the questionnaire."""
            target_idx = self.data['col_names'].index(start_col_search)
            entries = self.data['row_entries'][0][target_idx:]
            count = 0
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
        
        if not isinstance(self.options, list):
            raise ValueError("Options must be a list.")
        
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
    
    def generate_options_multi(self, questions: list[str] | None = None, q_idx: int = 0, start_col_search: str | None = None, num_of_cols: int = 2, col_adjust: str = "3.5in", col_format: str | None = None) -> str:
        """Generates the questionnaire with options column-wise. Only processes one question at a time."""
        if self.data is None:
            ClassWarnings.alert(ClassWarnings(NoDataFoundWarning), "Data not found. Cannot generate options for the questionnaire.")
            return ""

        get_key = list(self.format.keys())[0]

        @staticmethod
        def generate_question() -> str:
            """Generates the question for the questionnaire."""
            return f"\\footnotesize {get_key}.{q_idx + 1} & \\footnotesize {questions[q_idx]}" + '\n' if questions is not None else ""

        def generate_items(self) -> str:
            """Generates the items for the questionnaire."""
            target_idx = self.data['col_names'].index(start_col_search)
            entries = self.data['row_entries'][0][target_idx:]
            count = 0
            build_ques = ""
            for i, res in enumerate(self.options):
                k = (i + 1) % num_of_cols
                if res == "Others":
                    if entries[count+1] is not None:
                        name, flag = f"Others: {entries[count+1].strip()}", True
                    else:
                        name, flag = "Others", False
                    build_ques += make_tickbox(flag, name=name)
                elif entries[count] is None or res not in entries[count].split(','):
                    build_ques += make_tickbox(name=self.options[res])
                else:
                    build_ques += make_tickbox(True, name=self.options[res])

                if k == 0 and i != len(self.options) - 1:
                    build_ques += r" \\ " + '\n'
                elif i != len(self.options) - 1:
                    build_ques += " & "
                elif k != 0:
                    build_ques += " & " * (num_of_cols - k)

            build_ques += r" \\ " + '\n'
            count += 1
        
            return build_ques
        
        if self.options is None:
            raise ValueError("Options not found.")
        
        if not isinstance(self.options, dict):
            raise ValueError("Options must be a dictionary.")
        
        if start_col_search is None:
            raise ValueError("Column to search not found.")
        
        items_table = Tabular({get_key: "p{3cm}" * num_of_cols}) if col_format is None else Tabular({get_key: col_format})

        if questions is None:
            build_ques = ''.join([items_table.begin_table("H"),
                                items_table.toggle_centering(),
                                items_table.begin_adjustbox(col_adjust),
                                items_table.begin_tabular(get_key),
                                generate_items(self),
                                items_table.end_tabular(),
                                items_table.end_adjustbox(),
                                items_table.end_table()
                                ])
        else:
            build_ques = ''.join([self.table.begin_table("H"),
                                self.table.begin_adjustbox(r"\textwidth"),
                                self.table.begin_tabular(get_key),
                                generate_question(),
                                self.table.end_tabular(),
                                self.table.end_adjustbox(),
                                self.table.end_table(),

                                vertical_space("-2.25em"),

                                items_table.begin_table("H"),
                                items_table.toggle_centering(),
                                items_table.begin_adjustbox(col_adjust),
                                items_table.begin_tabular(get_key),
                                generate_items(self),
                                items_table.end_tabular(),
                                items_table.end_adjustbox(),
                                items_table.end_table()
                                ])

        return build_ques
    
    def generate_fill_blank(self, questions: list[str], q_start_idx: int = 0, q_end_idx: int = 99, start_col_search: str | None = None, col_format: str = r"\textwidth") -> str:
        """Generates the questionnaire with fill-in-the-blank answers."""
        if self.data is None:
            ClassWarnings.alert(ClassWarnings(NoDataFoundWarning), "Data not found. Cannot generate answers for the questionnaire.")
            return ""
        
        if questions is None:
            ClassWarnings.alert(ClassWarnings(NoQuestionsFoundWarning), "Questions not found. Cannot generate the questionnaire.")
            return ""

        get_key = list(self.format.keys())[0]

        def generate_items(self) -> str:
            """Generates the items for the questionnaire."""
            target_idx = self.data['col_names'].index(start_col_search)
            entries = self.data['row_entries'][0][target_idx:]
            i = q_start_idx + 1
            build_ques = ""
            for count, question in enumerate(questions[q_start_idx: q_end_idx + 1]):
                build_ques += f"\\footnotesize {get_key}.{i} & \\footnotesize {question} "
                build_ques += f"\\footnotesize \\textbf{{{entries[count] if entries[count] is not None else ''}}}"
                build_ques += r" \\ " + '\n'
                i += 1

            return build_ques
        
        if start_col_search is None:
            raise ValueError("Column to search not found.")
        
        build_ques = ''.join([self.table.begin_table("H"),
                              self.table.begin_adjustbox(col_format),
                              self.table.begin_tabular(get_key),

                              generate_items(self),

                              self.table.end_tabular(),
                              self.table.end_adjustbox(),
                              self.table.end_table()
                              ])
        
        return build_ques