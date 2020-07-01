__all__ = ['Coffee', 'Widget', 'widgets', 'kill', 'pid', 'start', 'restart']


import os
from ubersicht._coffee import Coffee
import listify
from ubersicht._widgets import Widget

WIDGETS = "%s/Library/Application Support/Übersicht/widgets" % os.environ[
    "HOME"]


def widgets():
    """return a list with widgets paths"""
    for l in os.listdir(WIDGETS):
        path = os.path.join(WIDGETS, l)
        if os.path.splitext(path)[1] == ".widget" and os.path.isdir(path):
            yield path


"""Übersicht.app process functions"""


def kill():
    """kill Übersicht.app process"""
    _pid = pid()
    if _pid:
        os.system("kill -9 %s &> /dev/null" % _pid)


def pid():
    """return Übersicht.app pid"""
    for l in os.popen("ps -ax").read().splitlines():
        if "Übersicht.app/Contents/MacOS/Übersicht" in l:
            return int(list(filter(None, l.split(" ")))[0])


def start():
    """open Übersicht.app"""
    if not pid():
        return os.system("open -a Übersicht")


def restart():
    """restart Übersicht.app"""
    kill()
    start()
