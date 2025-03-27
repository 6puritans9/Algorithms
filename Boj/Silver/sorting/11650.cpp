#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <utility>
#include <cstdio>

using namespace std;

/*
Problem:
N dots are given in 2D plane.
Sort the dots in ascending order of x-coordinate.
If x-coordinates are same, sort them in ascending order of y-coordinate.

Constraints:
Time Limit = 1000ms
Space Limit = 256MB
1. 1 <= N <= 10^5
2. -100,000 <= x, y <= 100,000
3. Coordinates are distinct integers.

Approach:
1. 10^5 only can only be solved in nlogn complexity.
2. Using quicksort, sort by x-coordinate.
3. Iterate N numbers with left and right(left+1)
4. If (numbers[left][0] == numbers[right][0]),
	expand right until they are not the same, or right >= N.
5. Sort by y-coordinate using quicksort.
6. left = right, right += 1
	if (right >= n) break;
7. Repeat

Complexity:
1. TC = O(2 * nlogn) = O(nlogn)
2. SC = O(1)

*/

void swap(vector<pair<int, int>>& dots_1, vector<pair<int, int>>& dots_2) {
	vector<pair<int, int>> temp = dots_1;
	dots_1 = dots_2;
	dots_2 = temp;
}

void quicksort_x(vector<pair<int, int>>& dots, int left, int right) {
	int pl = left;
	int pr = right;
	int pivot = dots[(left + right) / 2].first;

	while (pl <= pr) {
		while (dots[pl].first < pivot) {
			pl += 1;
		}
		while (dots[pr].first > pivot) {
			pr -= 1;
		}
		if (pl <= pr) {
			swap(dots[pl], dots[pr]);
			pl += 1;
			pr -= 1;
		}
	}

	if (pl < right) {
		quicksort_x(dots, pl, right);
	}
	if (left < pr) {
		quicksort_x(dots, left, pr);
	}
}

void quicksort_y(vector<pair<int, int>>& dots, int left, int right) {
	int pl = left;
	int pr = right;
	int pivot = dots[(left + right) / 2].second;

	while (pl <= pr) {
		while (dots[pl].second < pivot) {
			pl += 1;
		}
		while (dots[pr].second > pivot) {
			pr -= 1;
		}
		if (pl <= pr) {
			swap(dots[pl], dots[pr]);
			pl += 1;
			pr -= 1;
		}
	}

	if (pl < right) {
		quicksort_y(dots, pl, right);
	}
	if (left < pr) {
		quicksort_y(dots, left, pr);
	}
}

int main()
{
	int n;
	scanf("%d", &n);

	vector<pair<int, int>> dots(n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &dots[i].first, &dots[i].second);
	}

	quicksort_x(dots, 0, n-1);

	int left = 0;
	while (left < n) {
		int right = left + 1;
		while (right < n && dots[left].first == dots[right].first) {
			right += 1;
		}
		quicksort_y(dots, left, right-1);
		left = right;
	}

	return 0;
}
