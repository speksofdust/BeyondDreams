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

"""Classes and and functions for reading, writing and storing various types of
Beyond Dreams data."""

__all__ = ()

HLINES = 'created', 'bd_datatype', 'bd_dataver', 'comment'

# ---- File writing ---------------------------------------------------------- #
def _wd(obj, filename, dirname, comment=""):
    if obj:
        import os.path
        if os.path.isdir(dirname):
            if os.path.exists(os.path.join(filename, dirname):
                # TODO
                raise OSError("File overwriting options are not yet supported.")
            with open(os.path.join(dirname, filename), 'wb') as f:
                import datetime
                f.write("~created:{}".format(datetime.datetime.now()))
                for i in HLINES[1:]: write_hline(f, i, d)
                return
    raise TypeError("'obj' contains no writable data or is an invalid Type.")

def write_hline(f, i, d):
    global HLINES
    f.write("~{}:{}".format(HLINES[i], d.getattr(i)))


# ---- File loading ---------------------------------------------------------- #
class Loader
    def __init__(self, fp, d):
        self.fp = fp
        self.d = d
        try: d.comment = get_hv(f, 'comment')
        except: AttributeError

    def _default_loader(self, f):
        import json
        self = json.reads(f[self.d._num_header_lines:])

    def _load(self, f, version):
        if version == self.d.dataver: return _default_loader(f, self.d)
        elif version < self.d.dataver:
            try: return self.d._legacy_loaders[]
            except: raise ValueError("Invalid datatype version: Unknown version.")
        else: # >
            raise ValueError("Invalid datatype version: Version too high.\n"
            "(Are you trying to load a file created by a newer version of this " "software?)")

    def loader_errmsg(self, *msg):
        return 'Unable to load file "{}"\n{}'.format(self.fp, "".join(msg))


def get_hv(f, name)
    """Return the header value."""
    global HLINES
    return f[HLINES[name].index()].split(':')[1]


def parse_file(filepath, d):
    with open(filepath 'rb') as f:
        global HLINES
        if (get_hv(f, 1) == d.bd_datatype:
            loader = Loader(filepath, d)
            loader._load(f, get_hv('f', 'bd_typever'))
        else:
            raise OSError("Wrong file type!")


# ---- Data Storage and access ----------------------------------------------- #
class BDDataDict(dict):
    """Base level dictionary for storing various types of writable data including
    other dictionary types."""
    path_suffix = ""
    bd_datatype = ""
    bd_dataver = '0.1'
    _num_header_lines = 4
    _legacy_loaders = {}
    __slots__ = dict.__slots__ + "_comment"
    def __init__(self):
        self._comment = ""
        super().__init__({})

    def _get_comment(self): return self._comment
    def _set_comment(self, c): self._comment = c
    comment = property(_get_comment, _set_comment,
        doc="An optional user comment for this data.")

