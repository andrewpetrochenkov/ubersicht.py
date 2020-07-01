#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
from ubersicht._coffee import Coffee

WIDGETS = "%s/Library/Application Support/Übersicht/widgets" % os.environ["HOME"]


class Widget(Coffee):
    """widget generator class"""
    __readme__ = ["create", "rm"]
    name = None

    @property
    def path(self):
        """return widget path ~/Library/Application Support/Übersicht/widgets/name.widget"""
        return os.path.join(WIDGETS, "%s" % self.name)

    def create(self):
        """create widget"""
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        index = os.path.join(self.path, "index.coffee")
        open(index, "w").write(self.coffee())
        return self

    def rm(self):
        """remove widget (if exists)"""
        if os.path.exists(self.path):
            shutil.rmtree(self.path)
        return self

    def __str__(self):
        return '<Widget "%s">' % self.path
