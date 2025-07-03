#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int* d = new int[n];
    int sum = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> d[i];
        d[i] = clamp(d[i], 1, 1000);
        sum += d[i];
    }

    cout << sum << endl;

    delete[] d;
    return 0;
}