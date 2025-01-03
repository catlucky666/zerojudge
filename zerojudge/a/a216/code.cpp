#include <iostream>
using namespace std;
long long int f(int n){
    if(n == 1){
        return 1;
    }else{
        return n + f(n-1);
    }
}
long long int g(int n){
    if (n == 1){
        return 1;
    }else{
        return f(n) + g(n-1);
    }
}
int main(){
    long long int n;
    while (cin >> n){
        long long int re_f = f(n);
        long long int re_g = g(n);
        cout << re_f << " " << re_g << endl;
    }
    return 0;
}
