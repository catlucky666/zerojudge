#include<iostream>
using namespace std;
int main() {
	int a, b, c;
	int n, k;
	cin >> a >> b >> n;
	c = a + b;
	int to = 0;
	for (int i = 0; i < n; i++) {
		cin >> k;
		k = k % c;
		if (k >= a) {
			to += b - (k - a);
		}
	}
	cout << to << endl;
	return 0;
}