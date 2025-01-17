#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    int n;
    cin >> n; 
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }    
    sort(a.begin(), a.end());  
    bool isValid = true;
    for(int i = 1; i < n; i++){
        if(abs(a[i] - a[i - 1]) == 1){
            isValid = true;
        }else{
            isValid = false;
            break;
        }
    }   
    if(isValid){
        cout << a[0] << " " <<  a[n - 1] << " " << "yes" << endl;
    }else{
        cout << a[0] << " " <<  a[n - 1] << " " << "no" << endl;
    }
    return 0;
}