#include <iostream>
#include <algorithm>
using namespace std;

int countRightTriangles(int n, int len[]) {
    sort(len, len + n);
    int c = 0;
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (len[i] * len[i] + len[j] * len[j] == len[k] * len[k]) {
                    c++;
                }
            }
        }
    }
    return c; // 回傳 c 變數
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        int len[N];
        for (int i = 0; i < N; i++) {
            cin >> len[i];
        }
        int result = countRightTriangles(N, len);
        cout << result << endl;
    }
    return 0;
}
