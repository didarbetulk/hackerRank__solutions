#include <bits/stdc++.h>
using namespace std;

string larrysArray(const vector<int>& a) 
{
    long long inv = 0;
    int n = (int)a.size();
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            if (a[i] > a[j]) ++inv;
    return (inv % 2 == 0) ? "YES" : "NO";
}

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; 
    if (!(cin >> t)) return 0;
    while (t--) {
        int n; cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) cin >> a[i];
        cout << larrysArray(a) << "\n";
    }
    return 0;
}
//1den n'e kadar sayilardan olusan bir permutasyon var. 3 sirali eleman secerek saga veya sola dondur. amac: arrayi kucukten buyuge 3 sequential elelman dondurerek siralanabiliyor mu test etmek. 
//daha iyi bi cozum bulunabilir farklı zamanda tekrar coz.( python!! )
