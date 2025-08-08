import sys
class SAM:
    def __init__(self):
        self.next = [{}]         # transitions
        self.link = [-1]         # suffix links
        self.length = [0]        # max length for state
        self.last = 0

    def extend(self, ch):
        nxt = self.next
        link = self.link
        length = self.length

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

    # longest prefix of s[pos:] that is a substring of current text
    def longest_match_from(self, s, pos):
        v = 0
        L = 0
        n = len(s)
        nxt = self.next
        while pos + L < n:
            c = s[pos + L]
            t = nxt[v].get(c)
            if t is None:
                break
            v = t
            L += 1
        return L

def min_cost_for_string(s, A, B):
    sam = SAM()
    i = 0
    n = len(s)
    cost = 0
    while i < n:
        L = sam.longest_match_from(s, i)
        if L > 0 and B < A * L:
            # copy best we can (flat cost, so take all L)
            cost += B
            for k in range(L):
                sam.extend(s[i + k])
            i += L
        else:
            # append one character
            cost += A
            sam.extend(s[i])
            i += 1
    return cost

def main():
    data = [line.strip() for line in sys.stdin if line.strip() != ""]
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        N_str, A_str, B_str = data[idx].split()
        idx += 1
        s = data[idx]
        idx += 1
        A = int(A_str)
        B = int(B_str)
        out.append(str(min_cost_for_string(s, A, B)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
# 21 testten 6 tanesini gecti... simdiye kadar oluşturulan metni temsilen bir suffix automation (sam) yapısı tutuyor. 
#her adimda eklenmemmis kismin mevcut metinde zaaten gecen en uzun başlangıc parcasının(prefix)uzunlugunu buluyoruz ve bu uzunluk L oluyor.... 
