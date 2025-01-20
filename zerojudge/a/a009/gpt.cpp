#include <iostream>
#include <string>
using namespace std;

int main() {
    string code;  // 宣告一個字串變數
    cin >> code;  // 從使用者輸入讀取字串

    string decrypted = "";  // 初始化解密後的字串

    for (char c : code) {  // 遍歷字串的每個字元
        char trans = static_cast<char>(c - 7);  // 將字元的 ASCII 值減 7
        decrypted += trans;  // 加入解密字元到結果字串
    }

    cout << decrypted << endl;  // 輸出解密結果
    return 0;
}