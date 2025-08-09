import sys
from collections import deque

def read_input():
    it = iter(map(int, sys.stdin.read().strip().split()))
    N = next(it); M = next(it); K = next(it)
    bikers = [(next(it), next(it)) for _ in range(N)]
    bikes  = [(next(it), next(it)) for _ in range(M)]
    return N, M, K, bikers, bikes

def sqdist(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx*dx + dy*dy

def hopcroft_karp(adj, n, m, need):
    pairU = [-1] * n
    pairV = [-1] * m
    dist  = [0] * n

    def bfs():
        q = deque()
        for u in range(n):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1
        found_free = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found_free = True
        return found_free

    def dfs(u):
        for v in adj[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = -1
        return False

    matching = 0
    while bfs():
        for u in range(n):
            if pairU[u] == -1 and dfs(u):
                matching += 1
                if matching >= need:
                    return matching
    return matching

def solve():
    N, M, K, bikers, bikes = read_input()

    # Precompute all squared distances
    d = [[0]*M for _ in range(N)]
    maxd = 0
    for i in range(N):
        for j in range(M):
            dij = sqdist(bikers[i], bikes[j])
            d[i][j] = dij
            if dij > maxd:
                maxd = dij

    lo, hi = 0, maxd
    while lo < hi:
        mid = (lo + hi) // 2
        # Build adjacency for threshold mid
        adj = [[] for _ in range(N)]
        for i in range(N):
            row = d[i]
            adj[i] = [j for j in range(M) if row[j] <= mid]

        if hopcroft_karp(adj, N, M, K) >= K:
            hi = mid
        else:
            lo = mid + 1

    print(lo)

if __name__ == "__main__":
    solve()
# biker-bike ciftleri arasindaki karesel mesafelerle iki kumeli grafik kurup, binary search ve maksimum eslesme testiyle K bikerin en kisa surede bisiklete ulasabilecegi minimum zaman karesini buldum.
# VE BU TAM OLARAK 3 GUNUMU ALDİ...
