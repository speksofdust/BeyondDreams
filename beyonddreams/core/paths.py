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
_localcfg = None


def bd_datapath(*args):
    """Returns the absolute path of "beyonddreams/data/" joined with args."""
    return os.path.join(os.path.split(os.path.abspath(__file__)),
        "data", *args)

def localcfg_path(*args):
    """Returns the path of the local localcfg directory joined with args."""
    global _localcfg
    return os.path.join(_localcfg, *args)

def set_localcfg_path(path=None):
    """Set and verify the localcfg path. None uses 'os.environ['HOME'] and will'
    be something like 'home/myusername/.beyonddreams'"""
    global _localcfg
    if (path is None and _localcfg is None):
        tmp = os.path.join(os.environ['HOME'], '.beyonddreams')
        if not os.path.isdir(tmp): os.path.mkdir(tmp)
        _localcfg = tmp
    # TODO set custom path

def get_user_ids():
    """Return an iterator of all user ids."""
    return iter(i for i in os.listdir(localcfg_path('users')) if
        isdir(get_localcfg_path('users', i)))

def _user_mkdir(user, *args):
    if args:
        if not os.path.exists(user.datapath(*args):
            os.mkdir(user.datapath(*args)


def add_user():
    import datetime
    d = datetime.datetime.now()
    import random
    from .user import User
    user = User()
    while True:
        user._uid = str(random.randint(100000000, 99999999999999))
        if user._uid not in get_user_ids(): break
    try: os.mkdir(user.datapath())
    except:
        raise OSError('Unable to create directory: {}'.format(user.datapath())
    with open(user.datapath('ustats'), 'wb') as f:
        f.write(''.join('created : ', d)
    #with open(user.datapath('localcfg'), 'wb') as f:
    return user


def add_char(user):
    _user_mkdir('chardata')

