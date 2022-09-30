# Alex that his list of gemstones was mixed up.
# Alex is particularly fond of a certain type of gemstone and wants to move them to the end of his gallery display. Let’s design a recursive algorithm to help Alex set up his gallery

# define move_to_end() here
def move_to_end(lst, val):
  result = []
  if lst == []:
    return result #if list is empty, return empty list
  if lst[0] == val:
    result += move_to_end(lst[1:], val) #use lst[1:] as the argument here in order to bring the input closer to the base case
    result.append(lst[0]) #if first item matches val then we extract the first item from lst and append it to the end of the result  
   else:
    result.append(lst[0])
    result += move_to_end(lst[1:], val) #where the first item does NOT match val, we need to extract the first item from lst and append it to the beginning of result.
  return result # result will be a copy of lst with every instance of val moved to the end of the list.

#or
# def move_to_end(lst, val):
#   result = []
#   if len(lst) == 0:
#     return []
 
#   if lst[0] == val:
#     result += move_to_end(lst[1:], val)
#     result.append(lst[0])
#   else:
#     result.append(lst[0])
#     result += move_to_end(lst[1:], val)
 
#   return result
# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))
