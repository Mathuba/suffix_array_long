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


def test_compute_char_classes():
    text = "ababaa$"
    order = [6, 0, 2, 4, 5, 1, 3]
    result_class = suffix_array_long.compute_char_classes(text, order)
    assert result_class == [1, 2, 1, 2, 1, 1, 0]


def test_compute_char_classes_one():
    text = "AAA$"
    order = [3, 0, 1, 2]
    result_class = suffix_array_long.compute_char_classes(text, order)
    assert result_class == [1, 1, 1, 0]


def test_compute_char_classes_two():
    text = "GAC$"
    order = [3, 1, 2, 0]
    result_class = suffix_array_long.compute_char_classes(text, order)
    assert result_class == [3, 1, 2, 0]


def test_compute_char_classes_three():
    text = "AACGATAGCGGTAGA$"
    order = [15, 0, 1, 4, 6, 12, 14, 2, 8, 3, 7, 9, 10, 13, 5, 11]
    result_class = suffix_array_long.compute_char_classes(text, order)
    assert result_class == [1, 1, 2, 3, 1, 4, 1, 3, 2, 3, 3, 4, 1, 3, 1, 0]
