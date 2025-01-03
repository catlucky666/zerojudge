#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int d = 2 , c = 0;
    while(n > 1){
        if(n % d == 0){
            cout << d;
            n /= d;
            while(n % d == 0){
                c++;
                n /= d;
            }
            if(c > 0){
                cout << "^" << c + 1;
                c = 0;
            }
            if(n > 1){
                cout << " * ";
            }
        }else{
            d++;
            c = 0;
        }
    }
    cout << endl;
    return 0;
}
