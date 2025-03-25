#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>

using namespace std;

/*
	Problem:
	Sort the given N number in ascending order

	Constraints:
	1. 1 <= N <= 10^7
	2. 1 <= number <= 10^4
	3. Time Limit = 5000ms
	4. Space Limit = 8MB

	Approach:
	1. Although given N is very large 10^7, each element is relatively small, up to 10^4.
	2. Since the element is less than NlogN(10^7 * 23), counting sort is a feasible solution.
	3. Sort the numbers and print them line by line.

	*/

void print_counting_sorted(int n) {
	// TC = O(N+K) = 10^7 + 10^4 == 1000ms
	// SC = O(K) = 4bytes * 10^4 = 40000B == 40KB
	
	const int MAX_VALUE = 10000;
	int count_arr[MAX_VALUE + 1] = { 0 };

	int value;
	for (int i = 0; i < n; i++) {
		scanf("%d", &value);
		count_arr[value] += 1;
	}

	// apply prefix_sum,
	// which is redundant for this problem
	/*for (int j = 1; j < max_num + 1; j++) {
		count_arr[j] += count_arr[j - 1];
	}*/

	// print directly
	for (int i = 0; i < MAX_VALUE + 1; i++) {
		while (count_arr[i]--) {
			printf("%d\n", i);
		}
	}
}

int main() {
	int n;
	scanf("%d", &n);

	print_counting_sorted(n);

	return 0;
}
