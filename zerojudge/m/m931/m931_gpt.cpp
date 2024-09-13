#include <iostream>
#include <algorithm>
using namespace std;

// 定義一個結構來存儲 atk, def_, 和計算結果 b
struct Data {
    int b, atk, def_;
};

// 比較函數，用來排序
bool compare(const Data& a, const Data& b) {
    return a.b > b.b;
}

int main() {
    int n;
    cin >> n;

    Data A[100]; // 假設 n 最多不超過 100
    for (int i = 0; i < n; i++) {
        cin >> A[i].atk >> A[i].def_;
        A[i].b = A[i].atk * A[i].atk + A[i].def_ * A[i].def_;
    }

    // 排序
    sort(A, A + n, compare);

    // 輸出第二高的
    cout << A[1].atk << " " << A[1].def_ << endl;

    return 0;
}
