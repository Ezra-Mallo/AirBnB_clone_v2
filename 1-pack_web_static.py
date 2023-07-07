#!/usr/bin/env python3
"""
This is the do_pack function that creates the tgz version of a web_statics"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        timestmp = datetime.now().strftime("%Y%m%d%H%M%S")

        archive_name = "versions/web_static_{}.tgz web_static".format(timestmp)

        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))
#        local("tar -cvzf "+ archive_name)
#        return (archive_name)
        return "versions/web_static_{}.tgz".format(timestmp)
    except:
        return None
