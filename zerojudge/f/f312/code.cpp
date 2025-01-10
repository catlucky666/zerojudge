#include<iostream>
#include<cmath>
using namespace std;

int main() {
    int A1, B1, C1;
    int A2, B2, C2;
    cin >> A1 >> B1 >> C1;
    cin >> A2 >> B2 >> C2;
    int n;
    cin >> n;
    int X1, X2, Y1, Y2;
    int sum = -10000000;
    for(X1 = 0; X1 <= n; X1++) {
        X2 = n - X1;
        Y1 = (A1 * pow(X1, 2)) + B1 * X1 + C1;
        Y2 = (A2 * pow(X2, 2)) + B2 * X2 + C2;
        sum = max(sum, Y1 + Y2);
    }
    cout << sum << endl;
    return 0;
}
