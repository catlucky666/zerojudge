#include <iostream>
#include <vector>

using namespace std;

// 二分搜尋函數
bool binarySearch(const vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return true;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);  // 提高輸入輸出效率
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    vector<int> members(N);
    for (int i = 0; i < N; ++i) {
        cin >> members[i];
    }

    while (Q--) {
        int query;
        cin >> query;
        if (binarySearch(members, query)) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }

    return 0;
}
