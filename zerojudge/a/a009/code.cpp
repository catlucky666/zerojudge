#include<iostream>
#include<string>
using namespace std;
int main(){
	string code;
	string result = "";
	cin >> code;
	for (int i = 0 ; i < code.length() ; i++){
		result += code[i] - 7;
	}
	cout << result << endl;
	return 0;
}