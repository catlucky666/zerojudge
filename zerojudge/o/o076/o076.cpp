#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    int n , k = 1 , l = 1;
    cin >> n;
    int a[n];
    for(int i = 0 ; i < n ; i++){
        cin >> a[i];
    }
    for(int i = 1 ; i < n ; i++){
        if(a[i] <= a[i - 1]){
            k++;
            l = max(l , k);
        }else{
            k = 1;
        }
    }
    cout << l << endl;
    return 0;
}
