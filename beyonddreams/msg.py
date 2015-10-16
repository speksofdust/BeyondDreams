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

# msgcodes
NORMAL =        0
USER =          1   # user text
WHISPER =       2
USER_WHISPER =  3 # user whisper

SERVER =    10
ADMIN =     11  # admin message
ERROR =     12
WARN =      13


class _Channels(list):
    def __init__(self):
        pass

    def __del__(self):
        self.clear_all
        self = None

    def clear_all(self):
        """Clear all messages on all channels."""
        for i in self: i.clear

    def close_all(self):
        """Close all channels."""
        for i in self: i.close()

    def chans_with_unread(self):
        """Return an iterator of all channels with new messages."""
        return iter(i for i in self if i._unread >= 1)

    def clear_unread(self):
        """Reset the number of unread messages to 0 on all channels."""
        for i in self: i._unread = 0


class Chan(list):
    """Message channel class."""
    _default_msgcode = NORMAL
    def __init__(self, name):
        self._name =  name
        self._unread = 0

    def __del__(self):
        self = None
        self._name = None

    def clear(self):
        """Clear all messages."""
        self._items = [:]
        self._unread = 0

    @property
    def unread(self):
        """The number new messages since this channel was last viewed."""
        return self._unread

    def clear_unread(self):
        """Resets the number of unread messages to 0."""
        self._unread = 0

    @property
    def last_timestamp(self):
        """The last timestamp."""
        return self[-1].timestamp

    @property
    def last_message(self):
        """The last message."""
        return self[-1]

    def new_message(self, msg, msgcode='default'):
        """Append a new message to this channel."""
        if msg:
            if (msgcode == 'default' or not msgcode):
                self.append(Message(self._default_msgcode, msg)
            else self.append(Message(msgcode, msg))
            self._unread += 1

    def dump(self, filepath, append=True):
        """Dump all messages from this channel to a text file."""
        with open(filepath, 'wb') as f:
            for i in self:
                f.write(i.timestamp, i)

    def close(self):
        """Close this channel."""
        channels[self._name]


class Message(str):
    """Text message with timestamp."""
    def __init__(self, msgcode, *args, **kwargs):
        import time
        self._ts = int(time.time())
        self._msgcode = msgcode

    @classmethod
    def _from_str(self, s):
        """Create a message by parsing a text string. Used to load messages."""
        self._ts, self._msgcode = s.split(';')
        super().__init__(s.split(':')[1])

    def __str__(self): return "{};{}:{}".format(self._ts, self._msgcode, self)
    __repr__ = __str__

    @property
    def timestamp(self):
        """The timestamp for this message."""
        import datetime
        return datetime.datetime.fromtimestamp(self._ts)

