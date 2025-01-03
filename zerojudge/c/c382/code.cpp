#include<iostream>
using namespace std;

int main(){
    string str;
    int a,b;
    cin>>a>>str>>b;
    if(str == "+"){
    	cout<<a+b<<endl;
	}else if(str == "-"){
		cout<<a-b<<endl;
	}else if(str == "*"){
		cout<<a*b<<endl;
	}else if(str == "/"){
		cout<<a/b<<endl;
	}
	return 0;
}
