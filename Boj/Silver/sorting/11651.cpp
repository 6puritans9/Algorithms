#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>

using namespace std;

/*
Problem:
1. N points are given on a 2-dimensional plane
2. Sort them by y coordinate in ascending order.
3. if two points had same y coordinate, sort them by x coordinate in ascending order
4. No point has the identical coordinates
5. Print the sorted result

Constraints:
1. 1 <= N <= 10^5
2. -10^5 <= x, y ,+ 10^5
Time 1000ms
Space 256MB

Approach:
1. O(N^2) is not feasible.
2. Since the amount of given points are up to 10^5,
	using mergesort will require additioanl O(N) = 4bytes * 10^5 = 400KB
3. Time Complexity will be O(NlogN) = 10^5 * (log_10*10^5)*(log_10*2) = 10^5 * 1.5  == 1.5 * 5/8 * 10^3 = 2/3*5/8 * 10^3 <= 10^3 ms

Total Complexity:
TC = O(NlogN)
SC = O(N)
*/

struct Coord {
	int x;
	int y;
};

class Solution {
private:
	int n;
	vector<Coord> points;

	void merge(vector<Coord>& points, int left, int mid, int right) {
		vector<Coord> temp;
		int i = left;
		int j = mid + 1;

		// sort y, sort x
		while (i <= mid && j <= right) {
			if (points[i].y < points[j].y) {
				temp.push_back(points[i]);
				i++;
			}
			else if (points[j].y < points[i].y) {
				temp.push_back(points[j]);
				j++;
			}
			else {
				if (points[i].x < points[j].x) {
					temp.push_back(points[i]);
					i++;
				}
				else {
					temp.push_back(points[j]);
					j++;
				}
			}
		}

		while (i <= mid) {
			temp.push_back(points[i]);
			i++;
		}
		while (j <= right) {
			temp.push_back(points[j]);
			j++;
		}

		for (int i = 0; i < temp.size(); i++) {
			points[i + left] = temp[i];
		}
	}

	void merge_sort(vector<Coord>& points, int left, int right) {
		if (left >= right) {
			return;
		}

		int mid = (left + right) / 2;

		merge_sort(points, left, mid);
		merge_sort(points, mid + 1, right);
		merge(points, left, mid, right);
	}

public:
	Solution() {
		scanf("%d", &n);
		points.resize(n);
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &points[i].x, &points[i].y);
		}
	}

	void sort_points() {
		merge_sort(points, 0, n - 1);
	}

	void print_points() {
		for (Coord point : points) {
			printf("%d %d\n", point.x, point.y);
		}
	}
};

int main()
{
	Solution s;
	s.sort_points();
	s.print_points();

	return 0;
}
