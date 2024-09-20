#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
const int MAX = 1000000;
int main(){
    int n;
    int a[1000];
    int cost[1000][1000];
    cin >> n;
    for(int i = 0 ; i < n ; i++){
        cin >> a[i];
    }
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < n ; j++){
            cost[i][j] = (i == j) ? 0 : MAX;
        }
    }
    for(int l = 2 ; l <= n ; l++){
        for(int i = 0 ; i <= n - l ; i++){
            int j = (i + l) - 1;
            for(int k = i ; k < j ; k++){
                int sum1 = 0;
                for(int m = i ; m <= k ; m++){
                    sum1 += a[m];
                }
                int sum2 = 0;
                for(int m = k + 1 ; m <= j ; m++){
                    sum2 += a[m];
                }
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k + 1][j] + abs(sum1 - sum2));
            }
        }
    }
    cout << cost[0][n - 1] << endl;
    return 0;
}
