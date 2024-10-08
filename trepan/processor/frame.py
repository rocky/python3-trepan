# -*- coding: utf-8 -*-
#   Copyright (C) 2013-2014, 2024 Rocky Bernstein <rocky@gnu.org>
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
#
# Call-frame-oriented helper function for Processor. Put here so we
# can use this in a couple of processors.

from typing import Tuple

from trepan.lib.complete import complete_token
from trepan.processor.cmdfns import get_an_int

def frame_low_high(proc_obj, direction) -> Tuple[int, int]:
    stack_size = len(proc_obj.stack)  # - hide_level
    if direction is None:
        return (-stack_size, stack_size - 1)
    else:
        frame_index = proc_obj.curindex
        low, high = [
            frame_index * -direction,
            (stack_size - frame_index - 1) * direction,
        ]
        if direction < 0:
            low, high = [high, low]
        return (low, high)


def frame_complete(proc_obj, prefix, direction):
    low, high = frame_low_high(proc_obj, direction)
    ary = [str(low + i) for i in range(high - low + 1)]
    return complete_token(ary, prefix)


def frame_num(proc_obj, pos: int) -> int:
    return len(proc_obj.stack) - pos - 1


def adjust_frame(proc_obj, pos: int, is_absolute_pos: bool):
    """Adjust stack frame by pos positions. If is_absolute_pos then
    pos is an absolute number. Otherwise it is a relative number.

    A negative number indexes from the other end."""
    if not proc_obj.curframe:
        proc_obj.errmsg("No stack.")
        return

    # Below we remove any negativity. At the end, pos will be
    # the new value of proc_obj.curindex.
    if is_absolute_pos:
        if pos >= 0:
            pos = frame_num(proc_obj, pos)
        else:
            pos = -pos - 1
            pass
    else:
        pos += proc_obj.curindex
        pass

    if pos < 0:
        proc_obj.errmsg("Adjusting would put us beyond the oldest frame.")
        return
    elif pos >= len(proc_obj.stack):
        proc_obj.errmsg("Adjusting would put us beyond the newest frame.")
        return

    proc_obj.curindex = pos
    proc_obj.curframe = proc_obj.stack[proc_obj.curindex][0]
    proc_obj.location()
    proc_obj.list_lineno = None
    proc_obj.list_offset = proc_obj.curframe.f_lasti
    proc_obj.list_object = proc_obj.curframe
    proc_obj.list_filename = proc_obj.curframe.f_code.co_filename

    return


def adjust_relative(proc_obj, name: str, args, signum: int):
    if not proc_obj.stack:
        proc_obj.errmsg("Program has no stack frame set.")
        return False
    if len(args) == 1:
        count = 1
    else:
        count_str = args[1]
        low, high = frame_low_high(proc_obj, signum)
        count = get_an_int(
            proc_obj.errmsg,
            count_str,
            (
                f"The '{name}' command argument must eval to"
                f" an integer. Got: {count_str}"
            ),
            low,
            high,
        )
        if count is None:
            return
        pass

    adjust_frame(proc_obj, pos=signum * count, is_absolute_pos=False)
    return
