import suffix_array_long
import pytest


def test_sort_characters():
    text = "ababaa$"
    order = suffix_array_long.sort_characters(text)
    assert order == [6, 0, 2, 4, 5, 1, 3]

