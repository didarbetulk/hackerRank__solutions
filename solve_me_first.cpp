#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int d, b;
    cin >> d >> b;

    d = clamp(d, 1, 1000);
    b = clamp(b, 1, 1000);

    cout << d + b << endl;
    return 0;
}
