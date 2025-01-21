#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int a = 0 , b = 1;
    int c = 0;
    for(int i = 2 ; i <= n + 1 ; i++){
        c = a + b;
        a = b;
        b = c;
    }
    int w = a;
    int h = b;
    cout << w << ":" << h << endl;
    return 0;
}