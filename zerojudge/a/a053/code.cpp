#include<iostream>
using namespace std;
int main() {
	int n, s = 0;
	cin >> n;
	if (n < 10) {
		s = 6 * n;
	}
	else if (n < 20) {
		s = 6 * 10 + 2 * (n - 10);
	}
	else if (n < 40) {
		s = 6 * 10 + 2 * 10 + 1 * (n - 20);
	}
	else {
		s = 100;
	}
	cout << s << endl;
	return 0;
}