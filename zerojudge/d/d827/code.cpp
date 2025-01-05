#include<iostream>
int main() {
    int n;
    std::cin >> n;
    int a = n / 12;
    int b = n % 12;
    if (n >= 12) {
        std::cout << b * 5 + a * 50 << std::endl;
    }
    else {
        std::cout << n * 5 << std::endl;
    }
    return 0;
}