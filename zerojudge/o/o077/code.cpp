#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstring>
using namespace std;
int main(){
    int h , w , n;
    int r , c , t , x;
    cin >> h >> w >> n;
    int a[h][w];
    memset(a , 0 , sizeof(a));
    for(int i = 0 ; i < n ; i++){
        cin >> r >> c >> t >> x;
        for(int j = 0 ; j < h ; j++){
            for(int k = 0 ; k < w ; k++){
                if((abs(r - j) + abs(c - k)) <= t){
                    a[j][k] += x;
                }
            }
        }
    }
    for(int i = 0 ; i < h ; i++){
        for(int j = 0 ; j < w ; j++){
            cout << a[i][j] << " ";

        }
        cout << endl;
    }
}
