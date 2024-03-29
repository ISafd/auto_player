import os
import pickle

from ..state import State
from . import Backend


class LocalfileBackend(Backend):
    NAME = "localfile"

    def _get_filename(self) -> str:
        directory = os.getcwd()
        filename = f"{directory}//.autoplayer_{self.session}"
        return filename

    def save(self, state: State) -> None:
        filename = self._get_filename()
        if state.is_empty():
            os.remove(filename)
            return
        with open(filename, "wb") as file:
            pickle.dump(state, file)

    def load(self) -> State:
        filename = self._get_filename()
        if not os.path.exists(filename):
            state = State()
        else:
            with open(filename, "rb") as file:
                state = pickle.load(file)
        return state
