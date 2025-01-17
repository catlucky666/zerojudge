#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    int N, M;
    cin >> N >> M;
    vector<vector<int>> scores(N, vector<int>(M));
    for (int i = 0; i < N; ++i){
        for (int j = 0; j < M; ++j){
            cin >> scores[i][j];
        }
    }
    int bestStu = 0;
    int worstStu = 0;
    int best = -1;
    int worst = -1;
    for (int i = 0; i < N; ++i){
        int imp = 0;
        int reg = 0;

        for (int j = 1; j < M; ++j){
            if (scores[i][j] > scores[i][j-1]){
                imp += scores[i][j] - scores[i][j-1];
            } else if (scores[i][j] < scores[i][j-1]){
                reg += scores[i][j-1] - scores[i][j];
            }
        }
        if (imp > best || best == -1){
            best = imp;
            bestStu = i + 1;
        }
        if (reg > worst || worst == -1){
            worst = reg;
            worstStu = i + 1;
        }
    }
    cout << bestStu << endl << worstStu << endl;
    return 0;
}
