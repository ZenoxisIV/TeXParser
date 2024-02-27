# This file handles the possible instances wherein the output might not be as expected but still continues to execute the program.

import warnings
from typing import Type

class ClassWarnings:
    def __init__(self, IssueWarning: Type[UserWarning]) -> None:
        self.warning = IssueWarning

    def alert(self, message: str) -> None:
        warnings.formatwarning = lambda message, category, filename, lineno, line=None: f"{category.__name__}: {message}\n"
        warnings.warn(message, self.warning)

class NoTableFoundWarning(UserWarning):
    pass

class NoDataFoundWarning(UserWarning):
    pass

class NoQuestionsFoundWarning(UserWarning):
    pass

class NoOptionsFoundWarning(UserWarning):
    pass

