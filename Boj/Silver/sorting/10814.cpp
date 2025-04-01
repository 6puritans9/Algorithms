#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

/*
Problem:
For given N members, each row contains age and name.
1. Sort by age,
2. If two or more members have same age,
	keep their initial order
3. Print {"%s %s", &age, &name}

Constraints:
1. 1 <= N <= 10^5
2. 1 <= age <= 200
3. 1 <= name.length <= 10^2
Time 3000ms
Space 256MB

Approach:
1. Stable sort is crucial
2. Since the time limit is large enough, insertion sort O(N^2) can be a choice
3. I'll go for merge sort O(NlogN)

Total Complexity:
1. TC = O(NlogN) = 10^5 * 16 = 1.6 * 10^6 == 6/8 * 10^3 ms
2. SC = O(N) = 10^5 * (4 + 100)bytes == 10^7 bytes = 10MB

Note:
1. first submission with <iostream>
Mem 16184KB, Time 2760ms
2. second submission with <cstdio>, <cstring>
Mem 17836KB, Time 84ms

*/

class Solution {
private:
	int n;
	vector<pair<int, char*>> members;

	void merge(vector<pair<int, char*>>& arr, int low, int mid, int high) {
		vector<pair<int, char*>> temp;
		int left = low;
		int right = mid + 1;

		while (left <= mid && right <= high) {
			if (arr[left].first <= arr[right].first) {
				temp.push_back(arr[left]);
				left += 1;
			}
			else {
				temp.push_back(arr[right]);
				right += 1;
			}
		}

		while (left <= mid) {
			temp.push_back(arr[left]);
			left += 1;
		}

		while (right <= high) {
			temp.push_back(arr[right]);
			right += 1;
		}

		for (int i = low; i <= high; i++) {
			arr[i] = temp[i - low];
		}
	}

	void merge_sort(vector<pair<int, char*>>& arr, int left, int right) {
		if (left >= right) {
			return;
		}

		int mid = (left + right) / 2;
		merge_sort(arr, left, mid);
		merge_sort(arr, mid + 1, right);
		merge(arr, left, mid, right);
	}

public:
	Solution() {
		scanf("%d", &n);
		members.resize(n);
		for (int i = 0; i < n; i++) {
			members[i].second = new char[101];
			scanf("%d %s", &members[i].first, members[i].second);
		}
	}

	~Solution() {
		for (int i = 0; i < n; i++) {
			delete[] members[i].second;
		}
	}

	void sort_members() {
		merge_sort(members, 0, n - 1);
	}

	void print_members() const {
		for (const auto& member : members) {
			printf("%d %s\n", member.first, member.second);
		}
	}
};

int main()
{
	Solution s;
	s.sort_members();
	s.print_members();

	return 0;
}