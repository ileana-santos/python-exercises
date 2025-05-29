def first_half(s: str) -> str:
    """
    Returns the first half of a string with even length.

    Parameters:
    s (str): A string with an even number of characters.

    Returns:
    str: The first half of the input string.
    """
    # Return the substring from the start up to the halfway point
    return s[:len(s) // 2]
