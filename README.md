<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/ubersicht.svg?maxAge=3600)](https://pypi.org/project/ubersicht/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/ubersicht.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/ubersicht.py/actions)

### Installation
```bash
$ [sudo] pip install ubersicht
```

#### Examples
generate widget
```python
>>> import ubersicht
>>> widget = ubersicht.Widget(name="name.widget", command="echo hello world", refresh="1s",style="color: red")
>>> widget.create()
>>> widget.path
'/Users/username/Library/Application Support/Übersicht/widgets/name.widget'
```

```bash
$ cat ~/Library/Application Support/Übersicht/widgets/name.widget/index.coffee
command: "echo hello world"

refreshFrequency: '1s'

update: (output, domEl) ->
    $(domEl).empty().append("#{output}")

style: """
color: red
"""
```

#### Links
+   [Uebersicht.app](https://github.com/felixhageloh/uebersicht)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>