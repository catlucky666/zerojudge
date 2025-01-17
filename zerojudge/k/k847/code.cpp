#include<iostream>
using namespace std;
int main(){
    int m1 , d1 , m2 , d2;
    int days = 0;
    int mday[13]={0 , 31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31};
    cin >> m1 >> d1 >> m2 >> d2;
    if(m1 == m2){
        days = d2 - d1 + 1;
    }else{
        days = mday[m1] - d1 + 1;
        for(int i = m1 + 1 ; i < m2 ; i++){
            days += mday[i];
        }
        days += d2;
    }
    cout << (days - days / 10) * 100;
    return 0;
}
