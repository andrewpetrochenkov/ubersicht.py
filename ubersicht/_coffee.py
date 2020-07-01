#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _render(html):
    return '''
render: () -> """
%s
"""
'''.lstrip().rstrip() % html.lstrip().rstrip()


def _style(css):
    return '''
style: """
%s
"""
'''.lstrip().rstrip() % css.lstrip().rstrip()


def _update(value):
    return """update: (output, domEl) ->
    %s
""" % value.lstrip().rstrip()


class Coffee:
    """index.coffee generator class"""
    __readme__ = ["command", "refresh", "html", "update", "style"]
    command = "echo"
    refresh = '365 days'
    html = None
    update = '$(domEl).empty().append("#{output}")'
    style = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def refreshFrequency(self):
        return self.refresh

    @refreshFrequency.setter
    def refreshFrequency(self, value):
        self.refresh = value

    def coffee(self):
        """index.coffee source code"""
        items = [
            "command: \"%s\"" % self.command,
            "refreshFrequency: '%s'" % self.refresh
        ]
        if self.html:
            items += [_render(self.html)]
        items += ["""update: (output, domEl) ->
    %s""" % self.update]
        if self.style:
            items += [_style(self.style)]
        return "\n\n".join(items) + "\n"

    def __str__(self):
        return self.coffee()
