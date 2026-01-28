"""
Graph
- bfs
- dfs
- iterative deepning
- is_cyclic
- is_bipartite
- apply_dijksta
- apply_bellmanford
- union
- find_mst
- copy
- 
"""
from collections import deque

class GraphNode:
  def __init__(self , value , edges = []):
    self.value = value
    self.edges = edges

  def __call__(self):
    return self
      


class Graph:
  def __init__(self , *nodes):
    self.nodes = nodes

  def bfs(self , start_node_value = None):
    if not start_node_value:
      start_node_value = self.nodes[0].value

    visited = set()
    queue = []
    traversal_order = []

    queue.append(start_node_value)
    visited.add(start_node_value)

    while queue:
      current_node_value = queue.pop(0)
      traversal_order.append(current_node_value)

      current_node = next((node for node in self.nodes if node.value == current_node_value), None)
      
      if current_node:
        for neighbor in current_node.edges:
          if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    return traversal_order

  def dfs(self , start_node_value  = None):
    
    if not start_node_value:
      start_node_value = self.nodes[0].value

    visited = set()
    queue = deque()

    dfs_order = []

    queue.append(start_node_value)
    visited.add(start_node_value)

    while queue:

      current_node_value = queue.popleft()
      dfs_order.append(current_node_value)

      current_node = next((node for node in self.nodes if node.value == current_node_value) , None)

      if current_node:

        for n in current_node.edges:

          if n not in visited:
            visited.add(n)
            queue.appendleft(n)


    return dfs_order
    

if __name__ == "__main__":

  node_1 = GraphNode(1 , [2,3])()
  node_2 = GraphNode(2 , [1,4,5])()
  node_3 = GraphNode(3 , [1,5,6])()
  node_4 = GraphNode(4 , [2])()
  node_5 = GraphNode(5 , [2,3])()
  node_6 = GraphNode(6 , [3])()


  graph = Graph(node_1 , node_2 , node_3 , node_4 , node_5 , node_6)
  print(graph.bfs())
  print(graph.dfs())