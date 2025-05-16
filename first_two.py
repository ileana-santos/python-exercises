def first_two(str):
  """Returns the string made of its first two chars.

  Args:
    str: The input string.

  Returns:
    The first two characters of the string, or the original string if its length is less than 2.
  """
  if len(str) < 2:
    return str
  else:
    return str[:2]
