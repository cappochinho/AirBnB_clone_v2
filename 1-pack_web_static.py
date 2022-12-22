#!/usr/bin/python3
"""Generates a .tgz file from the contents of the web_static folder"""

from fabric import api
from datetime import datetime
import os

def do_pack():
    """
        Creates a tarball of webstatic files
        from the web_static folder in AirBnB_v2

        Return: the path of the .tgz file on success, else None
    """

    with api.settings(warn_only=True):
        dir = os.path.isdir('versions')
        if not dir:
            mkdir = api.local('mkdir versions')
            if mkdir.failed:
                return None
        
        suffix = datetime.now().strftime('%Y%m%d%M%S')
        path = 'versions/web_static_{}.tgz'.format(suffix)
        tar = api.local('tar -cvzf {} web_static'.format(path))
        if tar.failed:
            return None
        size = os.stat(path).st_size
        print('web_static packed: {} -> {}Bytes'.format(path, size))
        return path