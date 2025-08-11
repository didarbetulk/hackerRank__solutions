import sys
from array import array

def commonChild(s1: str, s2: str) -> int:
    m = len(s2)
    prev = array("H", [0] * (m + 1)) 

    for c1 in s1:
        curr = array("H", [0] * (m + 1))
        j = 1
        for c2 in s2:
            if c1 == c2:
                curr[j] = prev[j - 1] + 1
            else:
                a = prev[j]
                b = curr[j - 1]
                curr[j] = a if a >= b else b
            j += 1
        prev = curr

    return prev[m]

if name == "main":
    data = [line.rstrip("\n") for line in sys.stdin if line.strip() != ""]
    s1 = data[0]
    s2 = data[1]
    print(commonChild(s1, s2))
# longest common suubsequence(LCS) algoritmasinin kullanimina ornek bir soru. bellek kullanımını azaltmak icin yalnizca önceki(prev) ve mevcut(curr) satiri tutuyor O(n.m) zamanda ve O(m) bellekte sonuc uretiyor
