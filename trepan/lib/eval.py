# -*- coding: utf-8 -*-
#
#   Copyright (C) 2012-2015, 2023 Rocky Bernstein <rocky@gnu.org>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Things related to eval/exec"""

# extract the "expression" part of a line of source code.
#
import re


def extract_expression(text):
    if re.search(r"^\s*(?:if|elif)\s+", text):
        text = re.sub(r"^\s*(?:if|elif)\s+", "", text)
        text = re.sub(r":(?:\s+.*$|$)", "", text)
    elif re.search(r"^\s*assert\s+.*", text):
        # EXPR in : assert EXPRESSION:
        text = re.sub(r"^\s*assert\s+", "", text)
    elif re.search(r"^\s*(?:while)\s+", text):
        text = re.sub(r"^\s*(?:while)\s+", "", text)
        text = re.sub(r":(?:\s+.*$|$)", "", text)
    elif re.search(r"^\s*return\s+", text):
        # EXPRESSION in: return EXPRESSION
        text = re.sub(r"^\s*return\s+", "", text)
    elif re.search(r"^\s*for\s+.+\s+in\s+.*:", text):
        # EXPRESSION in: for VAR in EXPRESSION:
        text = re.sub(r"^\s*for\s+.+\s+in\s+", "", text)
        text = re.sub(":.*$", "", text)
    elif re.search(r"^\s*and\s+.*", text):
        # EXPRESSION in: and EXPRESSION
        text = re.sub(r"^\s*and\s+", "", text)
    elif re.search(r"^\s*or\s+.*", text):
        # EXPRESSION in: and EXPRESSION
        text = re.sub(r"^\s*or\s+", "", text)
    elif re.search(r"\s*[A-Za-z_][A-Za-z0-9_\[\]]*\s*=[^=>]", text):
        # RHS of an assignment statement.
        text = re.sub(r"^\s*[A-Za-z_][A-Za-z0-9_\[\]]*\s*=\s*", "", text)
        pass
    return text


# Demo it
if __name__ == "__main__":
    for stmt in (
        "if condition(x):",
        "elif _is_magic(name):",
        "while expression:",
        "for i in range(3):",
        "and x > 3",
        "or y < 3",
        "abc = 123",
        "return return_value",
        "nothing_to_be.done",
    ):
        print(extract_expression(stmt))
        pass
    pass
