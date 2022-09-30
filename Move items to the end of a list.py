# ###
# Alex is a gemstone collector who recently placed an order for an assortment of ambers, jades, pearls, and sapphires. When he opened the delivery package, Alex found that his list of gemstones was mixed up.
# ###

# ###
# Alex is particularly fond of a certain type of gemstone and wants to move them to the end of his gallery display. Let’s design a recursive algorithm to help Alex set up his gallery
# ###

# define move_to_end() here
def move_to_end(lst, val):
  result = []
  if lst == []:
    return result
  if lst[0] == val:
    result += move_to_end(lst[1:], val)
    result.append(lst[0])
  else:
    result.append(lst[0])
    result += move_to_end(lst[1:], val)
  return result
# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))
