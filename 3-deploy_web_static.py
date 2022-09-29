#!/usr/bin/python3
from fabric.operations import local, put, run
from fabric.api import env
import re
import os
from datetime import datetime
env.hosts = ['18.205.96.48', '3.231.218.163']
env.user = 'ubuntu'
env.identity = '~/.ssh/id_rsa'


def do_pack():
    """Function to compares"""
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static".format(
        time))
    if result.failed:
        return None
    return result


def do_deploy(archive_path):
    """Function to distribute an archive to a server"""
    if not os.path.exists(archive_path):
        return False
    try:
        rex = r'^versions/(\S+).tgz'
        match = re.search(rex, archive_path)
        filename = match.group(1)
        path = "/data/web_static/releases"
        put(archive_path, '/tmp/{}.tgz'.format(filename))
        run("mkdir -p {}/{}".format(path, filename))
        run("tar -xzf /tmp/{}.tgz -C {}/{}".format(filename, path, filename))
        run("mv {}/{}/web_static/* {}/{}".format(
            path, filename, path, filename))
        run("rm -rf {}/{}/web_static".format(path, filename))
        run("rm /tmp/{}.tgz".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current".format(path, filename))
        print("New version deployed!")
        return True
    except Exception:
        return True


def deploy():
    """Function to compares and to distribute an archive to a server"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
