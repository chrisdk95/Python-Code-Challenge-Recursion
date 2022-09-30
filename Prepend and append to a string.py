# Alex has picked out the gemstone that caught his friend’s fancy. He needs to wrap this fragile gemstone in wrapping paper before shipping it off to her. For our purpose, we will represent each layer of wrapping paper as "<>", so a pearl wrapped in 3 layers would be "<<<Pearl>>>". Let’s define a recursive function that wraps up a specified string in n layers of wrapping paper.

# define wrap_string() here
def wrap_string(str, n):
  result = ""
  if n <= 0:
    return str
  result += "<"
  result += wrap_string(str, n-1)
  result += ">"
 
  return result
# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)
