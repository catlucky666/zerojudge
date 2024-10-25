#include <iostream>
#include <vector>
#include <string>

void card_game(int n) {
    std::vector<int> cards; // 初始化牌堆
    std::vector<int> discarded; // 用於儲存丟掉的牌

    // 初始化牌堆
    for (int i = 1; i <= n; ++i) {
        cards.push_back(i);
    }

    // 當牌數大於1時持續操作
    while (cards.size() > 1) {
        discarded.push_back(cards.front()); // 丟掉最上面的那張牌
        cards.erase(cards.begin()); // 移除最上面的牌
        cards.push_back(cards.front()); // 將目前最上面的牌移到最底下
        cards.erase(cards.begin()); // 移除最上面的牌
    }

    int remaining_card = cards.front(); // 剩下的牌

    // 輸出結果
    std::cout << "Discarded cards: ";
    for (size_t i = 0; i < discarded.size(); ++i) {
        std::cout << discarded[i];
        if (i < discarded.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << std::endl;
    std::cout << "Remaining card: " << remaining_card << std::endl;
}

int main() {
    while (true) {
        int n;
        std::cin >> n;
        if (n == 0) {
            break; // 如果 n 為 0，則結束程式
        }
        card_game(n);
    }
    return 0;
}
