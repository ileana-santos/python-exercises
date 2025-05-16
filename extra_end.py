def extra_end(str):
  """Returns a new string made of 3 copies of the last 2 chars of the original string.

  Args:
    str: The input string (length will be at least 2).

  Returns:
    A new string formed by repeating the last two characters three times.
  """
  last_two = str[-2:]
  return last_two * 3
