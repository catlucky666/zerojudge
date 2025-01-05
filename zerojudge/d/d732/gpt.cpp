#include <iostream>
#include <vector>
#include <algorithm> // For binary_search and lower_bound
using namespace std;
// 二分搜尋，查找數字x在數列中的位置
int binarySearch(const vector<int>& A, int x) {
    auto it = lower_bound(A.begin(), A.end(), x);
    if (it != A.end() && *it == x) {
        return it - A.begin() + 1; // 返回1-based index
    }
    return 0; // 找不到的情況
}
int main() {
    int n, k;
    cin >> n >> k;
    vector<int> A(n);
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }
    vector<int> queries(k);
    for (int i = 0; i < k; ++i) {
        cin >> queries[i];
    }
    for (int x : queries) {
        cout << binarySearch(A, x) << endl;
    }
    return 0;
}