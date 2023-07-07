#!/usr/bin/env python3
"""
This is the do_pack function that creates the tgz version of a web_statics"""
from datetime import datetime
import fabric


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        timestmp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz web_static".format(timestmp)
        local("mkdir -p versions")
        local("tar -cvzf $archive_name")
        return (archive_name)
    except:
        return None
