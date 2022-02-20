from typing import Dict, Optional

from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo

from .lookup import Words
from .ui import Dialog

words_search = Words()


def __add_note(word, content):
    deck_id = mw.col.decks.get_current_id()
    model = mw.col.models.by_name("基本")
    n = mw.col.new_note(model)
    n["表面"] = word
    n["裏面"] = content
    _ = mw.col.add_note(n, deck_id)


def __add_notes(words: Dict[str, str]):
    for w, c in words.items():
        __add_note(w, c)


def __get_content(word: str) -> Optional[str]:
    c = words_search.query(word)
    return c


def add(text):
    lines = text.split("\n")
    n = len(lines)
    words = {}
    not_added = []
    for i in range(n):
        line = lines[i]
        if len(line) == 0:
            continue

        w = line.strip()
        c = __get_content(w)
        if c is None:
            not_added.append(c)
            continue

        words[w] = c

    __add_notes(words)
    mes = f"{len(words)} words were added."
    if len(not_added) > 0:
        mes += f"{len(not_added)} following word(s) were not added." + "\n".join(
            not_added
        )

    finished(mes)


def show_dialog():
    add_window.show()


def finished(mes):
    showInfo(mes)


add_window = Dialog()
add_window.pushed_add.connect(add)

mw.myWidget = add_window
action = QAction("Lookup EIJIRO", mw)
action.triggered.connect(show_dialog)
mw.form.menuTools.addAction(action)
