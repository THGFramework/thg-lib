from __future__ import absolute_import
from __future__ import division

from six.moves import configparser
import os

registered_configs = {}

def register_config(section, function):
    """Registers a configuration section.
    Arguments:
        section(str): Named configuration section
        function(callable): Function invoked with a dictionary of
            ``{option: value}`` for the entries in the section.
    """
    registered_configs[section] = function