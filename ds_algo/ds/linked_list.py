"""
To Do 
- Single LinkedList
- double LinkedList
- Circular LinkedList

functions
- reverse
- sort
- find
- append
- delete
- merge + merge k sorted list
- count
- copy

"""

numerics = int | float


class Node:  
  def __init__(self , value : numerics , next = None):

    self.value = value
    self.next = next
  


class LinkedList:

  def __init__(self , array : list[numerics]):

    self.head = Node(value=-1 , next=None)
    self.__init(array)
    
  def __init(self , array):

    first_node = Node(array[0] , None)
    self.head.next = first_node

    current_node = first_node

    for i in range(1 , len(array)):

      new_node = Node(array[i] , None)
      current_node.next = new_node

      current_node = new_node

  def printLL(self):

    curr_node : Node = self.head.next
    while(curr_node):
      print(curr_node.value , end=" -> ")
      curr_node = curr_node.next

    print("None")


if __name__ == "__main__":

  array = [i for i in range(0,10)]
  ll = LinkedList(array)

  ll.printLL()

