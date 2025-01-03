#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int result = (n > 0) ? 1 : ((n < 0) ? -1 : 0);
    cout << result << endl;
    return 0;
}
