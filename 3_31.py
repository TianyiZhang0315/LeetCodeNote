#1111
#有效括号的嵌套深度
def maxDepth(seq):
    if len(seq) == 0:
        return []
    d = 0
    ans = []
    for s in seq:
        if s == "(":
            d += 1
            ans.append(d % 2)
        elif s == ")":
            ans.append(d % 2)
            d -= 1
    return ans

print(maxDepth("((())())"))
