#include <iostream>
using namespace std;
int sum(int n) {
    int total = 0;
    for (int i = 1; i <= n; i += 2) {
        total += i;
    }
    return total;
}
int main() {
    int N;
    cin >> N;    
    int result = sum(N);
    cout << result <<endl;    
    return 0;
}