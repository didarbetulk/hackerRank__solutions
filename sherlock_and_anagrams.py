import sys
from collections import defaultdict

def sherlock_and_anagrams(s: str) -> int:
    n = len(s)
    # prefix sums of letter counts (26 lowercase letters)
    pref = [[0]*26 for _ in range(n+1)]
    for i, ch in enumerate(s, 1):
        ci = ord(ch) - ord('a')
        row = pref[i-1][:]
        row[ci] += 1
        pref[i] = row

    sig_counts = defaultdict(int)

   
    for l in range(n):
        for r in range(l+1, n+1):
            # signature = freq vector of substring
            freq = [pref[r][k] - pref[l][k] for k in range(26)]
            sig_counts[tuple(freq)] += 1

    
    total = 0
    for m in sig_counts.values():
        if m > 1:
            total += m * (m - 1) // 2
    return total

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    q = int(data[0].strip())
    out_lines = []
    for i in range(1, 1 + q):
        s = data[i].strip()
        out_lines.append(str(sherlock_and_anagrams(s)))
    sys.stdout.write("\n".join(out_lines))

if name == "main":
    main()
