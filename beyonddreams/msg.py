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

DEFAULT_MSG_SETTINGS = {
    'joinmsg':   r"/u Has joined.",
    'leavemsg':  r"/u Has left.",
    'timefmt':   "[%l:%M:%S]",
    'colors': {
        "normal":       "#CCCCCC",
        "user":         "#BFF0FF",
        "whisper_recv": "#7BA59E",
        "whisper_send": "#1E90FF",
        "user_warning": "#FF5600",
        "chan":         "#1A0000",
        "bot":          "#1AAFBB",
        "user_mentioned": "#757200",
        "important":    "#A5F378",
        "server":       "#757575",
        "admin":        "#800080",
        "help":         "#DDDDDD",
        "notice":       "#E5E545",
        "warn":         "#FFA500",
        "error":        "#FF0000",
        "divline":      "#CCCCCC"
        }
};

# msgcodes
NORMAL =        0   # normal text
USER =          1   # users own text
WHISPER_RECV =  2   # recieved whisper
WHISPER_SEND =  3   # sent whisper
USER_WARNING =  4   # warning text recieved by user (ie you are banned)
CHAN =          5   # for user joined/left/kicked/booted/banned etc.

USER_MENTIONED = 7 # text where own username was mentioned

INFO =          8
IMPORTANT =     9   # text marked as important
SERVER =        10  # server messages
ADMIN =         11  # admin message
NOTICE =        13
WARN =          14
ERROR =         15

# local
DIV_LINE =      20  # normal divider line
DIV_LINE_DASH = 21  # dashed divider line

BOT =           50  # channel bot
BOT2 =          51  # channel bot2

DIV_LINE_CODES = 20, 21

ALL_CODES = (0,1,2,3,4,5,6, 8,9, 10,11,12,13,14,15, 20,21, 50, 51)



import session

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


class GlobalChan:
    def __init__(self):
        pass

    def _get_default_codes(self):
        return session.user.config['msg-globchan-showcodes-default']
    def _set_default_codes(self, codes):
        session.user.config['msg-globchan-showcodes-default'] = list(set(codes))
    default_codes = property(_get_default_codes, _set_default_codes,
            doc="The default shown message codes.")

    def _get_shown(self):
        session.user.config['msg-globchan-showcodes-last']
    def _set_shown(self):
        session.user.config['msg-globchan-showcodes-last'] = list(set(codes))
    codes = property(_get_lastcodes, _set_lastcodes,
        "The currently shown message codes.")

    def hidden_codes(self):
        """Return an iterator of all currently hidden message codes."""
        return iter(i for i in ALL_CODES if i not in self.codes)

    def hide_codes(self, *codes):
        """Hide given codes."""
        self.codes = [i for i in self.codes if i not in codes]

    def show_codes(self, *codes):
        """Show given codes."""
        self.codes += codes

    def reset_codes(self):
        """Reset current codes to defaults."""
        self.codes = self.default_codes


class _Console(list):
    __slots__ = list.__slots__ + "_unread", "_closed"
    def __init__(self):
        self._unread = 0
        self._closed = False

    def clear(self):
        self._items = []
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
    def last(self):
        """The last message or log."""
        return self[-1]

    def add_div_line(self, code):
        if code in DIV_LINE_CODES:
            self.append(DivLine(code))

    def add_new(self, msg, msgcode='default'):
        """Append a new message to this channel."""
        if msg:
            if (msgcode == 'default' or not msgcode):
                self.append(Message(self._default_msgcode, msg))
            else: self.append(Message(msgcode, msg))
            self._unread += 1

    def _dump(self, filepath):
        """Dump all messages from this channel to a text file."""
        with open(filepath, 'wb') as f:
            f.write(self.name)
            for i in self:
                f.write(i.timestamp, i)

    def close(self):
        """Close this channel."""
        self._closed = True


class Chan(_Console):
    """Message channel class."""
    __slots__ = _Console.__slots__ + "_name"
    _default_msgcode = NORMAL
    def __init__(self, name):
        self._name =  name
        self._unread = 0
        self._closed = False

    def __del__(self):
        self = None
        self._name = None


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


class DivLine:
    """Text Divider Line"""
    __slots__ = "_msgcode"
    def __init__(self, msgcode):
        self._msgcode = msgcode

    def _get_divline(code, length):
        if code == DIV_LINE_DASH: return "-"*length
        else: return "—"*length


class Console(_Console):
    """Error console."""
    _default_msgcode = ERROR
    _default_verbosity = 2
    def __init__(self):
        self.name = "console"

    def log(self, msg, msgcode='default'):
        """Append a new message to this channel."""
        if msg:
            if (msgcode == 'default' or not msgcode):
                self.append(Message(self._default_msgcode, msg))
            else: self.append(Message(msgcode, msg))
            self._unread += 1

def _log_err(self, msg):
    if msg:
        self.append(Message(ERROR, msg))
        self._unread += 1

def _log_warn(self, msg):
    if msg:
        self.append(Message(WARN, msg))
        self._unread += 1

def _maxverbosity():
    import session
    try: return session._user['config']['console.verbosity']
    except: return Console._default_verbosity

def _log_info(self, msg, verbosity=2):
    if (msg and verbosity <= _maxverbosity()):
        self.append(Message(INFO, msg))
        self._unread += 1


Console.log.error = _log_err
Console.log.warn = _log_warn
Console.log.info = _log_info
