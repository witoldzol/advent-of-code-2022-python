nums = [51,71,17,24,42]

max = 0
for n in nums:
    for nn in nums:
        if n == nn:
            continue
        sum = n + nn
        sum_str = str(sum)
        same = all([i == sum_str[0] for i in sum_str])
        if same and sum > max:
            max = sum
print(f"{max=}")
