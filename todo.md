## DAY 16
- [x] calculate jumps to target
- [x] fix jump calculation
- each BFS has to have it's own map of visited nodes - it cannot be shared
  - [x] fix BFS test - make BFS use the visited map and not the visited property on the object
  - [x] remove visited property on the Valve object 
- [x] figure out a more elegant way of passing a map of visited nodes to BFS function, at the moment we create a fresh copy when starting a root invocation - this is not  a sustainable practice
- [x] calculate expected returns from all nodes based on current location
- [x] run 30 turn, recalculating with each move
- test the calculate_returns ( pay attention to case where you run out of turns )
  - [x] current test iterates over the empty node? examine that
  - [x] break up the function, or add comments, its difficult to reason about it
- improve the calculate_returns algo - it is not returning max possible value, perhaps we can run different scenarios where we do look ahead ( sum of two next moves etc )
  - [x] extract the loop outside, pass in the maps as params, and return them after each run?
  - [x] return a list of tuples ordered by potential returns
  - [x] return number of turns remaining with the tuple in function test_calculate_returns3_two_jumps
  - [x] manually verify that the test test_different_paths gives correct results 
  - [x] create a function that incorporates the above ( gets initials paths and then calculates returns for all subsequent paths and spits out the results )
    - [x] make the function take a number of top paths to retain, and explore their total returns.
    - [x] when we calculate returns for various paths, we need to be able to keep track of the path already taken ( start position and subsequent steps )
  - [x] use single step function to calculate returns for all possible routes
  - [x] fix total_flow calculation
  - [x] make a step function quickly return when out of turns or places to go
  - [x] simplify calculate_returns_for_a_single_turn -> it only needs to return initial expected returns or incorporate it in the version 2
  - [x] we want to detect within a step function if the path can continue any further ( ie, even if we still have turns left, there is no valve that we can reach )
  - [x] results contain duplicate paths - handle this ( run main with only 6 turns )
  - [x] fix BSF - it picks first path found, without considering other options, find all paths and pick the shortest [ edit: refactor BFS from being DFS to actually BFS ]
    after doing some research, I came to realise it makes no sense to calculate all paths.
    The issue wasn't that we picked the first path we found, the real issue was that we used depth first search not breadth first search algorithm.
    DFS explores paths one by one, to the end. If it finds the match, it returns. That's what was happening in this case, where the found path was not the shortest one.
  - [x] do version without graph - root has all the connections, so we should be able to do without it
  - [x] speed up the algo [ maybe limit the potential paths - because factorial is a real thing ??]
  - [x] speed up the bfs [ simple cache of bsf results was sufficient ]
  ### PART 2
  - [x] we need to iterate over 26 turns with a common VISITED map while keeping track of two pointers
    I think I will have to 'nest' the second pointer - first path , calc first option, than second taking account of where we already went?
    No idea
  - synchronize my path traversal with elephants
    at the moment we just make jumps from node to node, without considering how long it take 
    for example, I open B, elephant opens D - issue is , to open B takes 10 turns, to open D 2 turns, so elephants "waits" for my path to finish
    My initial thought is that my current implementation is not suitable to this type of a problem - I just jump from one node to another without going turn by turn
    I think we need a turn by turn implementation here ?
  [ ok, I think we can solve this by checking 'remaining_turns' on both paths in a tuple and evaluate a path that has more turns remaining - example: if my path has 10 turns remaining, and ele has 20, we will evaluate his path only, and return my old path with ele's new path ]
  [[ sample input gives correct answer but main input answer is too low, that's without implementiing synchronize]]
  - I've read some tips on how to solve part two - someone said they used bfs to print all paths - I've tried that and upon reflection realised it makes no sense.
    BFS would be a way to find paths to a target node, but not a way to permutate on each possible path
