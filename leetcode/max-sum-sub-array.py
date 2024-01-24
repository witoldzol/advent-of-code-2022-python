#https://leetcode.com/problems/max-pair-sum-in-an-array/solutions/3902240/using-map-detailed-approach-and-easy-to-understand-code/
nums = [31,25,72,79,74]
# nums = [51,71,17,24,42]
def maxSum(nums):
    max = -1
    max_digit = 0
    for n in nums:
        for nn in nums:
            if n == nn:
                continue
            sum = n + nn
            n_s = str(n)
            nn_s = str(nn)
            n_set = set([*n_s])
            print(f"set of {n} is {n_set}")
            nn_set = set([*nn_s])
            common = n_set & nn_set
            if common:
                print(f"Common between {n_set} and {nn_set} is {common}")
                for x in common:
                    if int(x) > max_digit:
                        max_digit = int(x)
                        print(f"Max didigt is {max_digit}")
                        max = sum
    print(f"MAX is = {max}")
    assert max == 146
    return max
print(maxSum(nums))
