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

FILETYPE_LINE = 1
COMMENT_LINE = 2

def _wd(obj, filename, dirname, comment=""):
    if obj:
        import os.path
        if os.path.isdir(dirname):
            if os.path.exists(os.path.join(filename, dirname):
                # TODO
                raise OSError("File overwriting options are not yet supported.")
            with open(os.path.join(dirname, filename), 'wb') as f:
                import datetime
                lw = datetime.datetime.now()
                f.write("~created:{}".format(lw))
                f.write("~bdfiletype:{}".format(obj.datatype)
                if comment: f.write("~comment:{}".format(comment))
                return
    raise TypeError("'obj' contains no writable data or is an invalid Type.")


def parse_file(filepath, d):
    with open(filepath 'rb') as f:
        c = 0
        global FILETYPE_LINE, COMMENT_LINE
        if not (f[FILETYPE_LINE].startswith("~bdfiletype") or
            f[FILETYPE_LINE].split(':') == d.datatype)
            raise OSError("Wrong file type!")
        d.comment = f[COMMENT_LINE].split(":")[1]
        import json
        self = json.reads(f[self._header_lines:])

class BDDataDict(dict):
    """Base level dictionary for storing various types of writable data including
    other dictionary types."""
    path_suffix = ""
    datatype = ""
    _header_lines = 3 # min 3 (created, filetype, commment)
    __slots__ = dict.__slots__ + "_comment"
    def __init__(self):
        self._comment = ""
        super().__init__({})

    def _get_comment(self): return self._comment
    def _set_comment(self, c): self._comment = c
    comment = property(_get_comment, _set_comment,
        doc="An optional user comment for this data.")

