# -*- coding: utf-8 -*-
#   Copyright (C) 2009-2010, 2013, 2015, 2020,
#   2024 Rocky Bernstein <rocky@gnu.org>
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

# Our local modules
from trepan.processor.command.base_subcmd import DebuggerSubcommand
from trepan.processor import cmdfns as Mcmdfns


class SetMaxString(DebuggerSubcommand):
    """**set maxstring** *number*

    Set the number of characters allowed in showing string values

    See also:
    ---------

    `show maxstring`"""

    in_list = True
    max_args = 1
    min_abbrev = len("str")  # Need at least "set max str"
    min_args = 1
    short_help = "Set maximum characters in showing strings"

    def run(self, args):
        Mcmdfns.run_set_int(
            self,
            " ".join(args),
            f"The '{self.name}' command requires a character count",
            0,
            None,
        )
        self.proc._repr.maxstring = self.settings[self.name]
        return None

    pass
