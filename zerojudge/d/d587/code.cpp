#include<bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }
    vector<int> count(3, 0);
    for (int num : numbers) {
        count[num - 1]++;
    }
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < count[i]; ++j) {
            cout << i + 1 << " ";
        }
    }
    return 0;
}