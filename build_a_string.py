import sys

class SAM:
    def __init__(self):
        self.next = [{}]
        self.link = [-1]
        self.length = [0]
        self.last = 0

    def extend(self, ch):
        nxt, link, length = self.next, self.link, self.length
        cur = len(nxt)
        nxt.append({})
        link.append(0)
        length.append(length[self.last] + 1)

        p = self.last
        while p != -1 and ch not in nxt[p]:
            nxt[p][ch] = cur
            p = link[p]

        if p == -1:
            link[cur] = 0
        else:
            q = nxt[p][ch]
            if length[p] + 1 == length[q]:
                link[cur] = q
            else:
                clone = len(nxt)
                nxt.append(nxt[q].copy())
                link.append(link[q])
                length.append(length[p] + 1)
                while p != -1 and nxt[p].get(ch, -1) == q:
                    nxt[p][ch] = clone
                    p = link[p]
                link[q] = link[cur] = clone
        self.last = cur

    # match up to cap first (quick check); if we reach cap, continue to max
    def longest_with_cap(self, s, pos, cap):
        v = 0
        L = 0
        n = len(s)
        nxt = self.next

        # try to reach cap quickly
        while L < cap and pos + L < n:
            c = s[pos + L]
            t = nxt[v].get(c)
            if t is None:
                return L, v  # fell short of cap
            v = t
            L += 1

        # if cap not reached, already returned
        # otherwise continue maximally
        while pos + L < n:
            c = s[pos + L]
            t = nxt[v].get(c)
            if t is None:
                break
            v = t
            L += 1
        return L, v

def min_cost_for_string(s, A, B):
    n = len(s)
    if B >= A:
        return A * n

    need = B // A + 1  # minimal length that makes copy cheaper than appends
    sam = SAM()
    cost = 0
    i = 0

    while i < n:
        L, _ = sam.longest_with_cap(s, i, need)
        if L >= need:
            # get full L already computed
            cost += B
            for k in range(L):
                sam.extend(s[i + k])
            i += L
        else:
            cost += A
            sam.extend(s[i])
            i += 1
    return cost

def solve():
    data = [line.strip() for line in sys.stdin if line.strip() != ""]
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        N_str, A_str, B_str = data[idx].split()
        idx += 1
        s = data[idx]
        idx += 1
        A = int(A_str); B = int(B_str)
        out.append(str(min_cost_for_string(s, A, B)))
    print("\n".join(out))

if name== "main":
    solve()

# 21 testten 6 tanesini gecti... simdiye kadar oluşturulan metni temsilen bir suffix automation (sam) yapısı tutuyor. 
#her adimda eklenmemmis kismin mevcut metinde zaaten gecen en uzun başlangıc parcasının(prefix)uzunlugunu buluyoruz ve bu uzunluk L oluyor.... 
#yeni haber. artik hic calismiyorr :)
