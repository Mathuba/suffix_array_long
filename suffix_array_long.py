# python3
import sys

CH_LEN = 256


def sort_characters(text_str):
    ts_len = len(text_str)
    counts = [0 for i in range(CH_LEN)]
    order = [None for i in range(ts_len)]

    # get the total number of individual items
    for char in text_str:
        counts[ord(char)] += 1

    # recompute starting positions in array to be returned (order)
    for j, _ in enumerate(counts):
        counts[j] = counts[j] + counts[j - 1]

    # load reversed characters (as ints) into order array
    for i in range(ts_len-1, -1, -1):
        c = ord(text_str[i])
        counts[c] = counts[c] - 1
        order[counts[c]] = i
    return order


def build_suffix_array(text):
    """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
    result = []
    # Implement this function yourself
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
