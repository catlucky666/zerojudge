#include<iostream>
#include<numeric>             //#
using namespace std;
int main(){
    int n;
    cin >> n;
    int a[n];
    for(int i = 0 ; i < n ; i++){
        cin >> a[i];
    }
    int sum = accumulate(a , a + n , 0);
    if(sum % 2 == 0){
        int t = sum / 2;
        bool dp[100001] = {false};
        dp[0] = true;
        for(int i = 0; i < n; i++){
            for(int j = t ; j >= a[i] ; j--){
                dp[j] = dp[j] || dp[j - a[i]];
            }
        }
        if(dp[t]){
            cout << "1" << endl;
        }else{
            cout << "0" << endl;
        }
    }else{
        cout << "0" << endl;
    }
    return 0;
}
