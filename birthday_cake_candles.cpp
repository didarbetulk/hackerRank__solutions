#include <iostream>
using namespace std;

int birthdayCakeCandles(int n) {
    int max_height = 0;
    int count = 0;
    int height;

    for (int i = 0; i < n; i++) 
    {
        cin >> height;
        if (height > max_height) 
        {
            max_height = height;
            count = 1;
        }
        else if (height == max_height) 
        {
            count++;
        }
    }
    return count;
}

int main() {
    int n;
    cin >> n;
    cout << birthdayCakeCandles(n) << endl;
    return 0;
}
