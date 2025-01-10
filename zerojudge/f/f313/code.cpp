#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int R, C, k, m;
    cin >> R >> C >> k >> m;
    int c[R][C];
    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            cin >> c[i][j];
        }
    }
    int dir[4][2] = {
        {-1 , 0},
        {1 , 0},
        {0 , -1},
        {0 , 1}
        };
    int n[R][C];
    for(int d = 0; d < m; d++){
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                n[i][j] = c[i][j];
            }
        }
        for(int i = 0; i < R; i++){
            for (int j = 0; j < C; j++){
                if(c[i][j] != -1){
                    int mov = c[i][j] / k;
                    for(int d = 0; d < 4; d++){
                        int ni = i + dir[d][0];
                        int nj = j + dir[d][1];
                        if(ni >= 0 && ni < R && nj >= 0 && nj < C && c[ni][nj] != -1){
                            n[ni][nj] += mov;
                            n[i][j] -= mov;
                        }
                    }
                }
            }
        }
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                c[i][j] = n[i][j];
            }
        }
    }
    int minp = 105;
    int maxp = -1;
    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            if(c[i][j] != -1){
                minp = min(minp, c[i][j]);
                maxp = max(maxp, c[i][j]);
            }
        }
    }
    cout << minp << '\n' << maxp << endl;
    return 0;
}