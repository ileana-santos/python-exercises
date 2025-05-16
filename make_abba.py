def make_abba(a, b):
  """Given two strings, a and b, return the result of putting them together
  in the order abba.

  Args:
    a: The first string.
    b: The second string.

  Returns:
    The string formed by concatenating a, b, b, and a.
  """
  return a + b + b + a
