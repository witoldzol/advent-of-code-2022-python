data = open("sample_input").read().strip()
lines = [x for x in data.split("\n")]
R = set()
for l in lines:
    prev = None
    for c in l.split("->"):
        c = c.strip()
        x, y = c.split(",")
        x, y = int(x), int(y)
        R.add((x, y))
        if prev:
            dx = x - prev[0]
            dy = y - prev[1]
            len_ = max(abs(dx), abs(dy))
            for i in range(len_):
                xx = prev[0] + (i * (1 if dx > 0 else (-1 if dx < 0 else 0)))
                yy = prev[1] + (i * (1 if dy > 0 else (-1 if dy < 0 else 0)))
                R.add((xx, yy))
        prev = (x, y)
# entrypoint
rock = (500, 0)
i = 0
drop = 0
while True:
    if rock in R:
        print("cant go any further")
        print(R)
        print(f"sand = {i}")
        break
    elif (rock[0], rock[1] + 1) not in R:
        rock = (rock[0], rock[1] + 1)
        print("moving down")
        drop += 1
        if drop > 300:
            print("im in the abbyss, ending here")
            break
        continue
    elif (rock[0] - 1, rock[1] + 1) not in R:
        rock = (rock[0] - 1, rock[1] + 1)
        print("moving left")
        continue
    elif (rock[0] + 1, rock[1] + 1) not in R:
        rock = (rock[0] + 1, rock[1] + 1)
        print("moving right")
        continue
    else:
        R.add((rock[0], rock[1]))
        print(f"sand rests in position = {rock}")
        i += 1
        rock = (500, 0)
        continue
print(f"added {i} pieces of sand")
