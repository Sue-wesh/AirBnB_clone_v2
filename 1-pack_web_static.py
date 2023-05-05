#!/usr/bin/python3
"""
generate a .tgz archive from the contents of the web_static folder of your 
AirBnB Clone repo, using the function do_pack"""
from fabric.api import local
import time

def do_pack():
    """generate a .tgz archive from the web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S")))

    except:
        return None
