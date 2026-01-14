"""
- Binary Tree


Function
- inorder , preorder , postorder
- invert
- max depth
- diameter
- checkBalance
- is_same
- is_subtree
- lowest_common_ancestor
- level order traversal
- right side and left side view
- good_nodes
- is_bst()
- 

- BST
  - insert
  - delete
  - max , min
  - kth min
  
"""

numerics = int | float 


class TreeNode:
    def __init__(self, val: numerics = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
  def __init__(self , array : list[numerics] = []):
    self.root = TreeNode(val=array[0])
    self.__build_tree(array=array)

  def __build_tree(self , array : list):

    len_array = len(array)     
    for i in range(1, len_array):

      if(not isinstance(array[i] , TreeNode)):        
        curr_node = TreeNode(array[i])
      else:
          curr_node = array[i]

      left_index = i * 2 + 1
      right_index = i * 2 + 2

      if(left_index < len_array):
        left_node = TreeNode(array[i*2 + 1])
        curr_node.left = left_node
        array[i*2 + 1] = left_node

      if(right_index < len_array):
        right_node = TreeNode(array[i*2 + 2])
        curr_node.right = right_node
        array[i*2 + 2] = right_node
      
      array[i] = curr_node
    

    self.root.left = array[1]
    self.root.right = array[2]


  def __inorder(self , root):
     
    def f(x : TreeNode):
      if(x is None) : return
      f(x.left)
      print(x.val , end=" -> ")
      f(x.right)
    
    f(root)
    print("None")  

  def print_tree(self, mode : str):
     if(mode == "inorder"):
        self.__inorder(self.root)
        


if __name__ == "__main__":
  
  array = [i for i in range(1,7)]
  bt = BinaryTree(array)

  bt.print_tree("inorder")




    