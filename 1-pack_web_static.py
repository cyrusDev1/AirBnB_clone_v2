#!/usr/bin/python3
from fabric.operations import local
from datetime import datetime


def do_pack():
    """Function to compares"""
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static".format(
        time))
    if result.failed:
        return None
    return result
