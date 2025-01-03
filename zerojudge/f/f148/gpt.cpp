#include <iostream>
#include <cstdlib>
using namespace std;
struct Target {
    char name;
    int row;
    int col;
};
int compareTargets(const void* a, const void* b) {
    return ((Target*)a)->name - ((Target*)b)->name;
}
int main() {
    int W, H, N;
    cin >> W >> H;
    cin >> N;
    char grid[10][10];
    for (int i = 0; i < W; ++i) {
        for (int j = 0; j < H; ++j) {
            cin >> grid[i][j];
        }
    }
    Target targets[26];
    int targetCount = 0;
    for (int i = 0; i < W; ++i) {
        for (int j = 0; j < H; ++j) {
            if (isalpha(grid[i][j])) {
                targets[targetCount] = {grid[i][j], i, j};
                targetCount++;
            }
        }
    }
    qsort(targets, targetCount, sizeof(Target), compareTargets);
    if (targetCount < N) {
        cout << "Mission fail." << endl;
    } else {
        for (int k = 0; k < N; ++k) {
            cout << targets[k].row << " " << targets[k].col << endl;
        }
    }
    return 0;
}
