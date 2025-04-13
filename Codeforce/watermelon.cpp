#include<iostream>

using namespace std;

int main(){
	int num;
	cin >> num;
	cout << (((num > 2) && ((num&1) == 0))? "YES": "NO") << endl;
	return 0;
}
