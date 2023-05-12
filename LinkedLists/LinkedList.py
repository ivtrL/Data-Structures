class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def reverse(self):
    current = self.head
    prev = None
    while current is not None:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev

  def print_list(self):
    i = self.head
    while i:
      print(i.data, end=" ")
      i = i.next


linkedList = LinkedList()

for j in range(5):
  k = float(input(f'Digite o {j+1}º número: '))
  linkedList.push(k)
print("List:")
linkedList.print_list()
linkedList.reverse()
print("\nReversed List:")
linkedList.print_list()
