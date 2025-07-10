def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(str(min_sum) + " " + str(max_sum))

arr = list(map(int, input().split()))
miniMaxSum(arr)
