#include <iostream>
using namespace std;
int main(){
    int N, Q;
    cin >> N >> Q;
    int mem[500000];
    for(int i = 0; i < N; ++i){
        cin >> mem[i];
    }
    while(Q--){
        int q;
        cin >> q;
        int l = 0;
        int r = N - 1;
        int found = 0;
        while(l <= r){
            int m = (l + r) / 2;
            if(mem[m] == q){
                cout << "Yes" << endl;
                found = 1;
                break;
            }else if(mem[m] < q){
                l = m + 1;
            }else{
                r = m - 1;
            }
        }
        if(found == 0){
            cout << "No" << endl;
        }
    }
    return 0;
}