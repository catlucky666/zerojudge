#include<iostream>
using namespace std;
int main(){
    int a , b;
    cin >> a >> b;
    int c = b - a;
    if(c > 0){
        cout << c << endl;
    }else{
        cout << c + 100 << endl;
    }
    return 0;
}
