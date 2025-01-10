#include <iostream>
using namespace std;
int main(){
    int a;
    cin >> a;
    char board[100][100];
    int result[100][100] = {0};
    for(int i = 0; i < a; i++){
        for(int j = 0; j < a; j++){
            cin >> board[i][j];
        }
    }
    int directions[8][2] = {
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1},          {0, 1},
        {1, -1}, {1, 0}, {1, 1}
    };
    for(int i = 0; i < a; i++){
        for(int j = 0; j < a; j++){
            if(board[i][j] == '*'){
                result[i][j] = -1;
                for(int k = 0; k < 8; k++){
                    int ni = i + directions[k][0];
                    int nj = j + directions[k][1];
                    if(ni >= 0 && ni < a && nj >= 0 && nj < a && result[ni][nj] != -1){
                        result[ni][nj]++;
                    }
                }
            }
        }
    }
    for(int i = 0; i < a; ++i){
        for(int j = 0; j < a; ++j){
            if(result[i][j] == -1){
                cout << '*';
            } else if(result[i][j] == 0){
                cout << '-';
            } else {
                cout << result[i][j];
            }
        }
        cout << endl;
    }
    return 0;
}
