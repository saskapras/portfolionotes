# === Stage 61: Add performance timing for core list and search operations ===
# Project: PortfolioNotes
import time
from typing import Any


def _timeit(func, *args, **kwargs) -> tuple:
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed_ms = (time.perf_counter() - start) * 1000
    return result, elapsed_ms


def list_all(notes, index=None):
    return _timeit(list, notes, index=index)


def find_by_id(notes, note_id):
    return _timeit(lambda notes, nid: [n for n in notes if n.id == nid], notes, note_id)


def find_by_tag(notes, tag):
    return _timeit(lambda notes, t: [n for n in notes if tag in n.tags], notes, tag)


def find_by_holding_id(notes, holding_id):
    return _timeit(lambda notes, hid: [n for n in notes if n.holding_id == hid], notes, holding_id)


def search_notes(notes, query):
    q = query.lower()
    return _timeit(lambda notes, q: [n for n in notes if q in str(n).lower()], notes, q)


def get_note_count(notes):
    return _timeit(len, notes)


def get_holding_count(notes):
    return _timeit(lambda n: len(set(n.holding_id for n in notes if n.holding_id)), notes)


def get_snapshot_count(notes):
    return _timeit(lambda n: len(set((n.holding_id, n.snapshot_date) for n in notes)), notes)


def get_reminder_count(notes):
    return _timeit(lambda n: len([n for n in notes if n.reminder_date]), notes)


def get_all_times(func, *args, **kwargs):
    times = []
    for _ in range(10):
        result, elapsed = _timeit(func, *args, **kwargs)
        times.append(elapsed)
    return times, result
