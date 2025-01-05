#include<iostream>
using namespace std;
int main(){
    int n;
    char a = '_';
    char b = '+';
    while(cin >> n){
        if(n == 0){
            break;
        }
        else{
            for(int i = 0 ; i < n ; i++){
                for(int j = i ; j < n - 1 ; j++){
                    cout << a;
                }
                for(int j = 0 ; j <= i ; j++){
                    cout << b;
                }
                cout << endl;
            }
        }
    }
}