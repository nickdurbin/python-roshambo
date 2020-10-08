'''
  Counting the components of a supergraph
  https://en.wikipedia.org/wiki/Component_(graph_theory)


  Create an undirected graph with depth first search aka dfs
  Create the graph from the input
    - There are points that are not accounted for in the graph
      - The edges and verticies of the grid.
  Find the shortest path from a vertex to itself.
    - If path shows atleast 3 veticies then stop looking
'''

def regionBySlashes(grid):
  