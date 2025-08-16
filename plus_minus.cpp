#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

void plusMinus(vector<int> arr) {
    int n = arr.size();
    int pos = 0, neg = 0, zero = 0;

    for (int num : arr) {
        if (num > 0) pos++;
        else if (num < 0) neg++;
        else zero++;
    }

    double posRatio = (double)pos / n;
    double negRatio = (double)neg / n;
    double zeroRatio = (double)zero / n;

    cout << fixed << setprecision(6) << posRatio << endl;
    cout << fixed << setprecision(6) << negRatio << endl;
    cout << fixed << setprecision(6) << zeroRatio << endl;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    plusMinus(arr);

    return 0;
}
