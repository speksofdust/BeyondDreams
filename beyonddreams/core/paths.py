# ---------------------------------------------------------------------------- #
#                                                                              #
#     This program is free software: you can redistribute it and/or modify     #
#     it under the terms of the GNU General Public License as published by     #
#     the Free Software Foundation, either version 3 of the License, or        #
#     (at your option) any later version.                                      #
#                                                                              #
#     This program is distributed in the hope that it will be useful,          #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#     GNU General Public License for more details.                             #
#                                                                              #
#     You should have received a copy of the GNU General Public License        #
#     along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                              #
# ---------------------------------------------------------------------------- #

import os
_cfgpath = None


def datapath(*args):
    """Returns the absolute path of "beyonddreams/data/" joined with args."""
    return os.path.join(os.path.split(os.path.abspath(__file__)),
        "data", *args)

def config_path(*args):
    """Returns the path of the local config directory joined with args."""
    global _cfgpath
    return os.path.join(_cfgpath, *args)

def set_config_path(path=None):
    """Set and verify the config path. None uses 'os.environ['HOME']'"""
    global _cfgpath
    if (path is NONE and _cfgpath is None): _cfgpath = os.environ['HOME']
    # TODO set custom path

def get_user_ids():
    """Return an iterator of all user ids."""
    return iter(i for i in os.listdir(config_path('users')) if
        isdir(config_path('users', i)))

def get_user_path(user_id, *args):
    """Return the users config path from a user id joined with args."""
    return config_path('users', user_id, *args)


def add_user():
    import datetime
    d = datetime.datetime.now()
    x = None
    import random
    while True:
        x = random.randint(100000000, 99999999999999)
        if x not in get_user_ids(): break
    try:
        os.mkdir(get_user_path(x))
        with open(get_user_path(x, 'ustats'), 'wb') as f:
            f.write(''.join('created : ', d)
        #with open(get_user_path(x, 'cfg'), 'wb') as f:

    except:
        raise OSError('Unable to open directory: {}'.format(
            config_path('users'))
    return x


def add_char(user_id):
    if not os.path.exists(user_id, 'chardata'):
        os.mkdir(get_user_path(user_id, 'chardata')
