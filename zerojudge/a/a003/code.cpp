#include <iostream>
using namespace std;
int main() {
    int M,D;
    cin >> M >> D;
    int S = (M * 2 + D) % 3;
    string fortune;
    if (S == 0) {
        fortune = "´¶³q";
    } else if (S == 1) {
        fortune = "¦N";
    } else {
        fortune = "¤j¦N";
    }
    cout << fortune << endl;
    return 0;
}
