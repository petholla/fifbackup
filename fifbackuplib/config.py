"""module to parse config files"""

import os
import configparser

def conf2dict(filename):

    """read config file and product a dict from it"""

    parser = configparser.ConfigParser()

    parser.read(filename)

    items = {}

    for section in parser:

        items[section] = {}

        for key, value in parser[section].items():

            items[section][key] = value

    return items

class Config:

    """Config class"""

    def __init__(self):

        self.home = os.getenv("HOME")

        self.conf_root = "{}/.fifbackup".format(self.home)
        self.targ_file = "{}/targets".format(self.conf_root)
        self.conf_file = "{}/config".format(self.conf_root)

        self._dirs = {}
        self._targets = {}

    @property
    def dirs(self):

        """return directories to backup"""

        if not self._dirs:

            self._dirs = conf2dict(self.conf_file)

        return self._dirs

    @property
    def targets(self):

        """return configured backupt targets"""

        if not self._targets:

            self._targets = conf2dict(self.targ_file)

        return self._targets
