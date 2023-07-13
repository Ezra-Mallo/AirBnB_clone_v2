#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""

from fabric import local
import time


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        sufix = time.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(sufix))
        return ("versions/web_static_{}.tgz".format(sufix))
    except Exception as e:
        return None
