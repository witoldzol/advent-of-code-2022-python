## DAY 16
- [x] calculate jumps to target
- [x] fix jump calculation
- each BFS has to have it's own map of visited nodes - it cannot be shared
  - fix BFS test - make BFS use the visited map and not the visited property on the object
  - remove visited property on the Valve object 
- figure out a more elegant way of passing a map of visited nodes to BFS function, at the moment we create a fresh copy when starting a root invocation - this is not  a sustainable practice
- calculate expected returns from all nodes based on current location
- run 30 turn, recalculating with each move
