Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

def string_splosion(str):
  result = ""
  for i in range(len(str) + 1):
    result += str[:i]
  return result

# Another way to do it
def string_splosion(str):
  return ''.join(str[:i] for i in range(len(str) + 1))

# Exercise from CodingBat
