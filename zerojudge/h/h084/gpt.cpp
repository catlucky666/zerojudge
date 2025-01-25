#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 检查给定高度 X 是否可以放置所有海报
bool canPlacePosters(const vector<int>& heights, const vector<int>& widths, int X) {
    int N = heights.size();
    int K = widths.size();
    int posterIndex = 0;

    for (int i = 0; i < N && posterIndex < K; ++i) {
        if (heights[i] >= X) {
            int segmentWidth = 0;
            while (i < N && heights[i] >= X) {
                ++segmentWidth;
                ++i;
            }
            // 处理在这个段内的海报
            while (posterIndex < K && widths[posterIndex] <= segmentWidth) {
                segmentWidth -= widths[posterIndex];
                ++posterIndex;
            }
        }
    }

    return posterIndex == K;
}

int main() {
    int N, K;
    cin >> N >> K;

    vector<int> heights(N);
    vector<int> widths(K);

    for (int i = 0; i < N; ++i) {
        cin >> heights[i];
    }

    for (int i = 0; i < K; ++i) {
        cin >> widths[i];
    }

    int low = 1;
    int high = *max_element(heights.begin(), heights.end());
    int result = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (canPlacePosters(heights, widths, mid)) {
            result = mid; // 这个高度有效，尝试更高的高度
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }

    cout << result << endl;

    return 0;
}