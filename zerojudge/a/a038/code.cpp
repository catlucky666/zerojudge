#include <iostream>
int main() {
    int num, reversedNum = 0;
    std::cin >> num;
    while (num != 0) {
        int digit = num % 10;
        reversedNum = reversedNum * 10 + digit;
        num /= 10;
    }
    std::cout << reversedNum << std::endl;

    return 0;
}
