def make_out_word(out, word):
  """Returns a new string where the word is in the middle of the out string.

  Args:
    out: A string of length 4 (e.g., "<<>>").
    word: The string to be placed in the middle.

  Returns:
    A new string with the word inserted in the middle of the out string.
  """
  return out[:2] + word + out[2:]
