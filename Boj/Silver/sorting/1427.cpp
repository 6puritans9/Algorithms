#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>

using namespace std;

/*
	Problem:
	For given integer N,
	sort each digit in descending order.

	Constraints:
	1. 1 <= N <= 10^9
	2. Time <= 2000ms
	3. Space <= 128MB

	Approach:
	1. Since N <= 10^9, covert N into an array digit by digit would be a feasible solution
	2. Assign an array with length n
	3. Sort in descending order with quicksort
	4. Print as a serialized string

	*/
class Solution {
private:
	void swap(vector<int>& arr, int pl, int pr) {
		int temp = arr[pl];

		arr[pl] = arr[pr];
		arr[pr] = temp;
	}

public:
	int get_length(int number) {
		int length = 0;

		while (number) {
			length += 1;
			number /= 10;
		}
		return length;
	}

	vector<int> convert_to_array(int number, int n) {
		vector<int> arr(n);
		int i = 0;

		while (number) {
			arr[i] = number % 10;
			i += 1;
			number /= 10;
		}

		return arr;
	}

	void quicksort(vector<int>& numbers, int left, int right) {
		// In descending order!
		if (left >= right) {
			return;
		}

		int pl = left;
		int pr = right;
		int pivot = numbers[(left + right) / 2];

		while (pl <= pr) {
			while (numbers[pl] > pivot) {
				pl += 1;
			}
			while (numbers[pr] < pivot) {
				pr -= 1;
			}
			if (pl <= pr) {
				swap(numbers, pl, pr);
				pl += 1;
				pr -= 1;
			}
		}

		quicksort(numbers, left, pr);
		quicksort(numbers, pl, right);
	}
};

int main() {
	// TC = O(NlogN)
	// SC = O(N)

	Solution s;

	int number;
	scanf("%d", &number);

	int n = s.get_length(number);
	vector<int> number_arr = s.convert_to_array(number, n);
	s.quicksort(number_arr, 0, n - 1);

	for (int i = 0; i < n; i++) {
		printf("%d", number_arr[i]);
	}

	return 0;
}