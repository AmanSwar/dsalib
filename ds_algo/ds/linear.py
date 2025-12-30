"""
Dynamic Array

Functions
- append (done)
- insert (done)
- get (done)
- pop (done)
- update (done)
- delete (done)
- sort
  - quick sort (done)
  - merge sort
  - bubble sort
  - insertion sort
- count 
- merge -> 2 options : sorted arr | alternative
- invert
- sum
  - 2 sum
  - 4 sum
- rotate
- longest common prefix
- min / max 
- top k frequent
- lognest consecutive seq
- subarray sum k 
- permute
- max subarray sum
- search
  - an element
  - first / last occurance

"""




from typing import Optional , Literal

class DynamicArray:

  def __init__(self , size : int = 100):

    self.buffer = [None] * size
    self.size = 0
    self.capacity = size

  def _resize(self) -> None:
    new_capacity = self.capacity * 2
    new_buffer = [None] * new_capacity

    self.buffer.append(new_buffer)
    self.capacity = new_capacity


  def append(self , value) -> None:
    if self.size == self.capacity: self._resize()

    self.buffer[self.size] = value
    self.size += 1

  def insert(self, index : int , value) -> None:
    if self.size == self.capacity: self._resize()

    for i in range(self.size , index , -1):
      self.buffer[i] = self.buffer[i - 1]

    self.buffer[index] = value
    self.size += 1

  def get(self , index : int) -> Optional[int]:
    if index < 0 or index >= self.size:
      return -1
    return self.buffer[index]

  def pop(self) -> Optional[int]:
    if self.size == 0:
      return -1
    
    value = self.buffer[self.size - 1]
    self.buffer[self.size - 1] = None
    self.size -= 1
    return value

  def update(self , index : int , value) -> None:
    self.buffer[index + 1] = value

  def delete(self , value , type : Literal["all" , "single" , "leave_1"]):

    if type == "all":
      for i in range(self.size):
        if self.buffer[i] == value:
          self.buffer[i] = None

    if type == "single":
      for i in range(self.size):
        if self.buffer[i] == value:
          self.buffer[i] = None
          break

    if type == "leave_1":

      flag : bool = True
      for i in range(self.size):

        if self.buffer[i] == value:

          if(flag):
            flag = False
            continue
          
          else:
            self.buffer[i] = None

    self.size -= 1

  def is_fragment(self):
    return (None in self.buffer[:self.size])

  def defragment(self):
    if not self.is_fragment():
      return

    write_index = 0

    for read_index in range(self.size):
      if self.buffer[read_index] is not None:
        self.buffer[write_index] = self.buffer[read_index]
        write_index += 1

    for i in range(write_index, self.size):
      self.buffer[i] = None

  def print_array(self):

    for i in range(self.size):

      if(self.buffer[i] == None):
        continue

      print(f"Index : {i} = {self.buffer[i]}")

  
  def quick_sort(self):#don't write code
    
    def _swap(index1 , index2):
      temp = self.buffer[index1]
      self.buffer[index1] = self.buffer[index2]
      self.buffer[index2] = temp

    def _partition(low , high):
      if(low >= high) : return
      
      mid = (low + high) // 2
      pivot_element = self.buffer[mid]

      i , j = low , high
      
      while(i <= j):
        while self.buffer[i] < pivot_element:
          i += 1

        while self.buffer[j] > pivot_element:
          j -= 1

        if (i <= j):
          _swap(i , j)
          low += 1
          high -= 1

      _partition(low , j)
      _partition(i , high)

    _partition(0 , self.size-1)

    

      

      

        


    

    


 


    


