import suffix_array_long
import pytest


def test_sort_characters():
    text = "ababaa$"
    order = suffix_array_long.sort_characters(text)
    assert order == [6, 0, 2, 4, 5, 1, 3]


def test_sort_characters_genome_one():
    text = "AAA$"
    order = suffix_array_long.sort_characters(text)
    assert order == [3, 0, 1, 2]


def test_sort_characters_genome_two():
    text = "GAC$"
    order = suffix_array_long.sort_characters(text)
    assert order == [3, 1, 2, 0]


def test_sort_characters_genome_three():
    text = "AACGATAGCGGTAGA$"
    order = suffix_array_long.sort_characters(text)
    assert order == [15, 0, 1, 4, 6, 12, 14, 2, 8, 3, 7, 9, 10, 13, 5, 11]


