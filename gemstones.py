def gemstones(arr):
    common = set(arr[0])
    for s in arr[1:]:
        common &= set(s)
    return len(common)

if __name__ == "__main__":
    n = int(input().strip())
    arr = [input().strip() for _ in range(n)]
    print(gemstones(arr))
