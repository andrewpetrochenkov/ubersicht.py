#!/usr/bin/env python
import ubersicht


class Coffee(ubersicht.Coffee):
    command = 'echo "hello world"'
    refresh = "1s"
    style = """
    top: 10px
    left: 10px
    color: #fff
    font-family: Helvetica Neue
"""

    @property
    def update(self):
        return """$(domEl).empty().append("#{output}")"""


coffee = Coffee(html="<div class='content'></div>")
print(coffee)
