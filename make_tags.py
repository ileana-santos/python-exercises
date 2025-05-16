def make_tags(tag, word):
  """Creates an HTML string with tags around the word.

  Args:
    tag: The HTML tag to use (e.g., "i", "cite").
    word: The word to be enclosed within the tags.

  Returns:
    T
  return "<" + tag + ">" + word + "</" + tag + ">"
