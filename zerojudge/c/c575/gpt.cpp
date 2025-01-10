#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 檢查是否可以使用給定的直徑和基地台數目覆蓋所有服務點
bool canCoverAllPoints(const vector<int>& points, int k, int diameter) {
    int count = 1; // 開始時使用一個基地台
    int currentCoverEnd = points[0] + diameter;

    for (int point : points) {
        if (point > currentCoverEnd) {
            count++;
            currentCoverEnd = point + diameter;
            if (count > k) {
                return false;
            }
        }
    }
    return true;
}

// 使用二分搜尋來找到最小的直徑
int findMinDiameter(int n, int k, vector<int>& positions) {
    sort(positions.begin(), positions.end());
    int low = 1, high = positions.back() - positions.front();

    while (low < high) {
        int mid = (low + high) / 2;
        if (canCoverAllPoints(positions, k, mid)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }

    return low;
}

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> P(N);

    for (int i = 0; i < N; i++) {
        cin >> P[i];
    }

    int minDiameter = findMinDiameter(N, K, P);
    cout << minDiameter << endl;

    return 0;
}
