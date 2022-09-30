# A friend asks Alex if she could buy a gemstone from his gallery. Alex agrees to remove any gemstone and sell it to her. How can he delete the i-th node from the linked list recursively?

import LinkedList

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

# define remove_node() here
def remove_node(head, i):
  if i < 0:
    return head
  if head is None:
    return None
  if i == 0:
    return head.next_node
  head.next_node = remove_node(head.next_node, i - 1)
  return head

# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)
print(head.flatten())
