def permutationEquation(p):
    n = len(p)
    result = []
    for x in range(1, n + 1):
        y1 = p.index(x) + 1
        y = p.index(y1) + 1
        result.append(y)
    return result

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
    for y in result:
        print(y)
