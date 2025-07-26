def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n + 1))
    if n % (2 * k) != 0:
        return [-1]
    result = []
    add = True
    for i in range(1, n + 1):
        if add:
            result.append(i + k)
        else:
            result.append(i - k)
        if i % k == 0:
            add = not add
    return result

# Input reading
t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    res = absolutePermutation(n, k)
    print(" ".join(map(str, res)))
