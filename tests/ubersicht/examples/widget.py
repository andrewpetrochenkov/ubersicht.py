#!/usr/bin/env python
import ubersicht


class Widget(ubersicht.Widget):
    command = "echo hello world"
    refresh = "1s"
    style = "color: red"


widget = Widget(name="name.widget")
print(widget.coffee())
widget.create()
print("path: %s" % widget.path)
