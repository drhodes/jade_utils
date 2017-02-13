import os

JADE_ZIP_URL = "https://github.com/6004x/jade/archive/master.zip"
JADE_UTIL = os.path.expanduser("~/jade_utils/")

def sub_path(subp):
    return os.path.expanduser(JADE_UTIL + subp)

JADE_ZIP = sub_path("jade-master.zip")
JADE_EXTRACT = sub_path("jade_master")
JADE_IMPORTS = sub_path("imports")
JADE_EXPORTS = sub_path("exports")
JADE_BACKUPS = sub_path("backups")

JADE_SERVER_MODULE = sub_path("jade_master/jade-master/server.py")
JADE_SERVER_DIR = sub_path("jade_master/jade-master")
