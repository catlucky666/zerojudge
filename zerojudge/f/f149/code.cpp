#include <iostream>
using namespace std;
int x, y, detected = 0, undetected = 0;
int map[20][20];
int main() {
    // 读取输入
    cin >> y >> x;
    for(int i = 0; i < y; i++) {
        for(int j = 0; j < x; j++) {
            cin >> map[j][i];
        }
    }

    // 探测炸弹
    for(int i = 0; i < y; i++) {
        for(int j = 0; j < x; j++) {
            switch(map[j][i]) {
                case 0:
                    break;
                case 1:
                    break;
                default:
                    for(int m = j-1; m <= j+1; m++) {
                        for(int n = i-1; n <= i+1; n++) {
                            if(m >= 0 && m < x && n >= 0 && n < y && !(m == j && n == i)) {
                                if(map[m][n] >= 5) {
                                    map[m][n] = 6;
                                    map[j][i] = 6;
                                }
                            }
                        }
                    }
                    if(map[j][i] == 5) {
                        for(int m = j-1; m <= j+1; m++) {
                            for(int n = i-1; n <= i+1; n++) {
                                if(m >= 0 && m < x && n >= 0 && n < y) {
                                    if(map[m][n] == 1) {
                                        detected++;
                                        map[m][n] = 0;
                                    }
                                }
                            }
                        }
                    }
                    break;
            }
        }
    }

    // 统计未探测到的炸弹
    for(int i = 0; i < y; i++) {
        for(int j = 0; j < x; j++) {
            if(map[j][i] == 1) {
                undetected++;
            }
        }
    }
    // 输出结果
    cout << detected << " " << undetected;
    return 0;
}
