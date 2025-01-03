#include <iostream>
int calculateGCD(int a, int b) {
    if (b == 0) {
        return a;
    }
    return calculateGCD(b, a % b);
}
int main() {
    int num1, num2;
    std::cin >> num1;
    std::cin >> num2;
    int gcd = calculateGCD(num1, num2);
    std::cout<< gcd << std::endl;
    return 0;
}
