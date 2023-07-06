#!/usr/bin/env python3
from datetime import datetime

timestamp=datetime.now().strftime("%Y%m%d%H%M%S")
archive_name = "web_static_{}.tgz".format(timestamp)
print(archive_name)
