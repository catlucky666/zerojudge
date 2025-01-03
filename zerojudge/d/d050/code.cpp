#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int a = n - 15;
    int b = (a + 24) % 24;
    cout << b << endl;
    return 0;
}
