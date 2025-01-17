#include<iostream>
using namespace std;
int main(){
    int n , s , a;
    cin >> n;
    int l[2][n],pro[n];
    for(int i = 0 ; i < 2 ; i++){
        for(int j = 0 ; j < n ; j++){
            cin >> l[i][j];
        }
    }
    s = l[0][0] * l[1][0];
    for(int i = 0 ; i < n ; i++){
        pro[i] = l[0][i] * l[1][i];
        if(pro[i] < s){
            s = pro[i];
            a = i;
        }
    }
    cout <<l[0][a] << " " << l[1][a];
    return 0;
}