def utopianTree(n):
    height = 1
    for i in range(1, n + 1):
        if i % 2 == 1:
            height *= 2
        else:
            height += 1
    return height

t = int(input())
for _ in range(t):
    n = int(input())
    print(utopianTree(n))
