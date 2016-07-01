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

class _Prompts(list):
    """Class for storing active prompts. Active prompts are stored in order of
    which they appeared. If multiple prompts they must be closed in reverse
    order."""

    def _clear_ok_prompts(self):
        for i in self:
            if i._prompt_type = "OK":
                del self[i]

_prompts = _Prompts


class Prompt:
    """Base class for Beyonddreams Prompt objects."""
    _prompt_type = "prompt"
    def __init__(self, text, buttons, default_btn_idx):
        self._text = text
        if isinstance(buttons, str): self._buttons = (buttons,)
        else: self._buttons = tuple(buttons)
        self._default_btn_idx = default_btn_idx
        _prompts.append(self)
        self._closed = False
        self._pressed_idx = -1

    def get_input(self):
        while True:
            if self._closed: break
            # wait for user input
            # FIXME
            else: return self._on_btn_release(self._pressed_idx)


    def _on_btn_release(self, i):
        """Overridden by each prompt type. One of these conditions must occur:
        mouse inside button and same button released
        keyboard key press (hotkey)
        """
        pass
        

    def _close(self):
        self._closed = True
        del _prompts[self]


class QuitPrompt(Prompt):
    _prompt_type = "quit"
    def __init__(self, text):
        Prompt.__init__(text, buttons=("quit", "cancel"), default_btn_idx=1)

    def _on_btn_release(self, i):
        self._close
        if i == 0: return True
        return False

class OKPrompt(Prompt):
    _prompt_type = "OK"
    def __init__(self, text):
        Prompt.__init__(text, buttons=("OK",), default_btn_idx=0)

    def _on_btn_release(self, i):
        self._close
        return 1

class ErrorPrompt(OKPrompt):
    _prompt_type = "error"
    def __init__(self, text):
        Prompt.__init__(text, buttons=("OK",), default_btn_idx=0)


