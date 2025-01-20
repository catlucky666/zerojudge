#include <iostream>
#include<cmath>
using namespace std;
int main() {
    long long int a, b;
    while (cin >> a >> b) {
        long long int c = abs(a - b);
        cout << c << endl;
    }
}