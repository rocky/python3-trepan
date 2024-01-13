#!/usr/bin/env python
"Unit test for trepan.processor.command.pr"

import inspect

from trepan import debugger
from trepan.processor.command.p import PCommand


def test_p():
    errors = []
    msgs = []

    def errmsg(msg_text: str):
        errors.append(msg_text)
        return

    def msg(msg_text: str):
        msgs.append(msg_text)

    return

    d = debugger.Trepan()
    cp = d.core.processor
    cp.curframe = inspect.currentframe()
    cmd = PCommand(cp)
    cmd.msg = msg
    cmd.errmsg = errmsg

    me = 10  # NOQA
    cmd.run([cmd.name, "me"])
    assert "10" == msgs[-1]
    cmd.run([cmd.name, "/x", "me"])
    assert "'0xa'" == msgs[-1]
    cmd.run([cmd.name, "/o", "me"])
    assert "'0o12'" == msgs[-1]
    return
