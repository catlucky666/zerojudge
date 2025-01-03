#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    cout << n << endl;
    int a;
    while(cin >> a){
    int b = (a * (a - 1) / 2) + 1;
    cout << b << endl;
    }
    return 0;
}
