#include<iostream>
#include<vector>

using namespace std;

int main() {
	vector <int> list(3,0);
	cout << list[-1];
	for(int n: list){
		cout<< n;
	}
	return 0;
}
