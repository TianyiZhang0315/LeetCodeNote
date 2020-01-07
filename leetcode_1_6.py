# re-order to obtain power of 2
from collections import Counter
def reorderedPowerOf2_v1(N):
    # make sure first num is not 0
    # for any binary number, if it is the power of 2, it only has one '1' in it.
    # itertools.permutation returns a iterator contains all permutations of input param
    # any() returns true if one of the element is true
    return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))
def reorderedPowerOf2_v2(N):
    count = Counter(str(N))
    # 1*(2**b) can also be 1<<b (first convert left to binary,
    # then move the number to the left by b positions)
    return any([count == Counter(str(1*(2**b))) for b in range(31)])
print(reorderedPowerOf2_v2(6))
