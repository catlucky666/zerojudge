#include<iostream>
#include<algorithm>
using namespace std;
int arr[1000005];
int N, K;
bool check(int a){
    int k = K;
    int pv = arr[0];
    for(int i = 1 ; i < N ; i++){
        if(arr[i] - pv > a){
            k--;
            pv = arr[i];
        }
    }
    k--;
    return k >= 0;
}
int Search(const int arr[] , int n,  int k){
    int l = 1;
    int r = arr[n - 1] - arr[0];
    while(l < r) {
        int m = l + (r - l) / 2;
        if(check(m)){
            r = m;
        } else {
            l = m + 1;
        }
    }
    return l;
}
int main(){
    cin >> N >> K;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    sort(arr , arr + N);
    int r = Search(arr , N , K);
    cout << r << '\n';
    return 0;
}
