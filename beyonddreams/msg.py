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


class _Channels:
    def __init__(self):
        self._items = {}

    def __del__(self):
        self.clear_all
        self._items = None

    def clear_all(self):
        """Clear all messages on all channels."""
        for i in self._items: i.clear

    def close_all(self):
        """Close all channels."""
        for i in self._items: i.close()

    def chans_with_unread(self):
        """Return an iterator of all channels with new messages."""
        return iter(i for i in self._items if i._unread >= 1)


class Chan:
    """Message channel class."""
    def __init__(self, name):
        self._name =  name
        self._items = items
        self._unread = 0

    def __eq__(self, x):        return x is self
    def __ne__(self, x):        return x is not self
    def __hash__(self, x):      return hash(id(self))
    def __len__(self):          return len(self._items)
    def __iter__(self):         return iter(self._items)
    def __getitem__(self, i):   return self._items[i]
    def __reversed__(self):     return reversed(self._items)
    
    def __del__(self):
        self._items = None
        self._name = None

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
        return self._items[-1].timestamp

    @property
    def last_message(self):
        """The last message."""
        return self._items[-1]

    def new_message(self, msg):
        """Append a new message to this channel."""
        if msg: self._items.append(Message(msg))
        self._unread += 1

    def clear_all(self):
        """Clear all messages."""
        self._items = [:]
        self._unread = 0

    def dump(self, filepath, append=True):
        """Dump all messages to a text file."""
        with open(filepath, 'wb') as f:
            for i in self._items:
                f.write(i.ts_format)

    def close(self):
        """Close this channel."""
        channels._items[self._name]


class Message(str):
    """Text message with timestamp."""
    def __init__(self, *args, **kwargs):
        import time
        self._ts = int(time.time())

    @property
    def timestamp(self):
        """The timestamp for this message."""
        import datetime
        return datetime.fromtimestamp(self._ts)
