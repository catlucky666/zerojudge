#include <iostream>
bool Year(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}
int main() {
    int year;
    while (std::cin >> year) {
        if (Year(year)) {
            std::cout << "¶|¦~" << std::endl;
        } else {
            std::cout << "¥­¦~" << std::endl;
        }
    }
    return 0;
}
