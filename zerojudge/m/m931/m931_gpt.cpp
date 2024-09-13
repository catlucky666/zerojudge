#include <iostream>
#include <algorithm>
using namespace std;

// �w�q�@�ӵ��c�Ӧs�x atk, def_, �M�p�⵲�G b
struct Data {
    int b, atk, def_;
};

// �����ơA�ΨӱƧ�
bool compare(const Data& a, const Data& b) {
    return a.b > b.b;
}

int main() {
    int n;
    cin >> n;

    Data A[100]; // ���] n �̦h���W�L 100
    for (int i = 0; i < n; i++) {
        cin >> A[i].atk >> A[i].def_;
        A[i].b = A[i].atk * A[i].atk + A[i].def_ * A[i].def_;
    }

    // �Ƨ�
    sort(A, A + n, compare);

    // ��X�ĤG����
    cout << A[1].atk << " " << A[1].def_ << endl;

    return 0;
}
