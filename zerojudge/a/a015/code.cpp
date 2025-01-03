#include<iostream>
using namespace std;
int main(){
  int r , c;
  while(cin >> r >> c){
    int m[r][c];
    for(int i = 0 ; i < r ; i++){
      for(int j = 0 ; j < c ; j++){
        cin >> m[i][j];
      }
    }
    for(int j = 0 ; j < c ; j++){
      for(int i = 0 ; i < r ; i++){
        cout << m[i][j] << " ";
        }
          cout << endl;
      }
   }
   return 0;
}
