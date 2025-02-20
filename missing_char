# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).

# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'

def missing_char(str, n):
  return str[:n] + str[n + 1:]

#Explanation
# s[:n] gets all characters before index n.
# s[n+1:] gets all characters after index n.
# Concatenating them removes the character at index n.

# Exercise from CodingBat
