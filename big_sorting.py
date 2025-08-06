def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))

if __name__ == "__main__":
    n = int(input())
    unsorted = [input().strip() for _ in range(n)]
    result = bigSorting(unsorted)
    for num in result:
        print(num)
