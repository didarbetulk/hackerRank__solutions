#include <iostream>
using namespace std;

long long bigsum(int n) {
    long long sum = 0;
    long long num;
    for (int i = 0; i < n; i++) {
        cin >> num;
        sum += num;
    }
    return sum;
}

int main() {
    int n;
    cin >> n;

    if (n < 1 || n > 10)
    {     
        return 1; 
    }

    cout << bigsum(n) << endl;
    return 0;
}
