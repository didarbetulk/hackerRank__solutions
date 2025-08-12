import sys

def is_sorted(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))

def almostSorted(arr):
    n = len(arr)

    # find first index where order breaks
    l = 0
    while l < n - 1 and arr[l] <= arr[l + 1]:
        l += 1
    if l == n - 1:
        print("yes")
        return

    # find last index where order breaks
    r = n - 1
    while r > 0 and arr[r] >= arr[r - 1]:
        r -= 1

    # try swap (preferred over reverse)
    b = arr[:]
    b[l], b[r] = b[r], b[l]
    if is_sorted(b):
        print("yes")
        print("swap", l + 1, r + 1)
        return

    # try reverse
    seg = arr[l:r + 1]
    if seg == sorted(seg, reverse=True):
        c = arr[:l] + list(reversed(seg)) + arr[r + 1:]
        if is_sorted(c):
            print("yes")
            print("reverse", l + 1, r + 1)
            return

    print("no")

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    almostSorted(arr)

if name == "main":
    main()
# dizideki ilk ve son siralama bozulma noktalarini bulup once bu iki elemani swap ederek,olmazsa aradaki bölümü reverse ederek sıralamaiı deniyor
  #eger iki yontemden biri ise yararsa "yes" ve işlemi, yoksa "no" yazdiriyor
