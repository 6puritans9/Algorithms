#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>

using namespace std;

/*
Problem:
1. N coordinates are given on a line.
2. Compressed coords X'i is the number of Xjs that satisfies Xi > Xj.
3. Print each X'n on a single line split by " ".

Constraints:
TIME 2000ms
SPACE 512MB
1. 1 <= N <= 10^6
2. -10^9 <= Xi <= 10^9

Approach:
1. Simple O(N^2) is not feasible
2. Sort the given coords in NlogN time
3. For each Xi, use binary search logN to find the rank

Total Complexity:
1. TC = O(NlogN + N + NlogU) <= O(2NlogN + N) = O(NlogN) = (10^6 * (6*1.8)) < 2000ms
2. SC = O(N) = 4bytes * 10^6 == 4MB

*/
struct Unique {
	int rank;
	int value;
};


class Solution {
private:
	int n;
	vector<int> points;

	void swap(vector<int>& arr, int pl, int pr) {
		int temp = arr[pl];
		arr[pl] = arr[pr];
		arr[pr] = temp;
	}

	void quicksort(vector<int>& arr, int left, int right) {
		if (left >= right) {
			return;
		}

		int pl = left;
		int pr = right;
		int pivot_value = arr[(left + right) / 2];

		while (pl <= pr) {
			while (arr[pl] < pivot_value) {
				pl++;
			}
			while (arr[pr] > pivot_value) {
				pr--;
			}

			if (pl <= pr) {
				swap(arr, pl, pr);
				pl++;
				pr--;
			}
		}

		quicksort(arr, left, pr);
		quicksort(arr, pl, right);
	}

	vector<int> create_sorted(vector<int>& points) {
		vector<int> sorted(n);
		for (int i = 0; i < n; i++) {
			sorted[i] = points[i];
		}

		quicksort(sorted, 0, n - 1);

		return sorted;
	}

	int find_rank(vector<Unique>& uniques, int target) {
		int left = 0;
		int right = uniques.size() - 1;

		while (left <= right) {
			int mid = (left + right) / 2;

			if (uniques[mid].value == target) {
				return uniques[mid].rank;
			}
			else if (uniques[mid].value < target) {
				left = mid + 1;
			}
			else {
				right = mid - 1;
			}
		}

		return -1;
	}

public:
	Solution() {
		scanf("%d", &n);
		points.resize(n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &points[i]);
		}
	}

	void compress() {
		// preserve points in sorted state
		vector<int> sorted = create_sorted(points);
		
		// extract unique numbers
		vector<Unique> uniques;
		int rank = 0;

		for (int i = 0; i < n; i++) {
			if (i == 0 || sorted[i] != sorted[i - 1]) {
				Unique u;
				u.rank = rank++;
				u.value = sorted[i];

				uniques.push_back(u);
			}
		}

		// mutate points
		for (int i = 0; i < n; i++) {
			int target = points[i];

			points[i] = find_rank(uniques, target);
		}
	}

	void print_all() {
		for (int point : points) {
			printf("%d ", point);
		}
	}


};

int main()
{
	Solution s;

	s.compress();
	s.print_all();
	return 0;
}
