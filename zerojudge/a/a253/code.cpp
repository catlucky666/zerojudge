#include iostream>
using namespace std;
int main(){
    int S1, S2;
    int S[100] = {0};
    while(cin >> S1){
        if(S1 == -1){
            break;
        }
        cin >> S2;
        if(S1 >= 0 && S1 < 101){
            S[S1] += S2;
        }
    }
    while(cin >> S1){
        if(S1 == -1){
            break;
        }
        cin >> S2;
        if(S1 >= 0 && S1 < 101){
            S[S1] += S2;
        }
    }
    for(int i = 0; i < 100; i++) {
        if(S[i] > 0) {
            cout << i << " " << S[i] << endl;
        }
    }
    return 0;
}
