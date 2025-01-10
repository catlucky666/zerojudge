#include <iostream>
using namespace std;
int main(){
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        int N;
        cin >> N;
        int w[50];
        for(int j = 0 ; j < N ; j++){
            cin >> w[j];
        }
        int high = 0 , low = 0;
        for(int i = 1 ; i < N ; i++){
            if(w[i] > w[i - 1]){
                high++;
            }else if(w[i] < w[i - 1]){
                low++;
            }
        }
        cout << "Case " << t << ": " << high << " " << low << endl;
    }
    return 0;
}