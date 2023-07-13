#!/usr/bin/python3

from fabric.api import local
from time import strftime
"""Generates a .tgz archive from the contents of the web_static folder."""


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    timestamp = strftime("%Y%m%d%H%M%S")
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -czvf versions/web_static_{}.tgz web_static/"
              .format(timestamp))

        return "versions/web_static_{}.tgz".format(timestamp)

    except Exception as e:
        return None
