#include <iostream>
#include <vector>
using namespace std;

void swap(int* num1, int* num2){
	*num1 = *num1 + *num2;
	*num2 = *num1 - *num2;
	*num1 = *num1 - *num2;
}

int main() {
	int n, k;	
	cin >> n >> k;
	
	vector<int> scores(n);
	for (int i =0; i<n; i++){
		cin >> scores[i];
	}
	
	for (int i = 0; i < n-1; i++){
		for (int j = 0; j < n-1-i; j++){
			if (scores[j] < scores[j+1]){
				swap(&scores[j], &scores[j+1]);
			}
		}
	}
	
	cout << scores[k-1];		

	return 0;
}