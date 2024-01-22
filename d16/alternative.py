from typing import Tuple
from collections import deque

valves = {}
tunnels = {}
dists = {}

def bfs(start: Tuple[int, str], target: str) -> int:
    queue = deque()
    queue.append(start)
    visited = set()
    while queue:
        distance, node_name = queue.popleft()
        if node_name == target:
            return distance
        for neighbour in tunnels[node_name]:
            if neighbour in visited:
                continue
            queue.append((distance + 1, neighbour))
    raise Exception(f"Unable to find a path from {start[1]} to {target}")

# parse input
input = "input"
# input = "sample_input"
for line in open(input):
    line = line.strip()
    valve = line.split()[1]
    flow = int(line.split(";")[0].split("=")[1])
    targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
    valves[valve] = flow
    tunnels[valve] = targets

# calculate distances between non zero nodes
for valve, flow in valves.items():
    # skip zero nodes
    if valve != "AA" and flow == 0:
        continue
    dists[valve] = {}
    for v,f in valves.items():
        if v != "AA" and f == 0 or v == valve:
            continue
        dists[valve][v] = bfs((0,valve), v)

print(dists)
