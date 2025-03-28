#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

/*
Problem:
1. An array of integers "citations" given
2. citations[i] = the number of citations a researcher received for their i-th paper
3. Get the h-index, which is
4. maximum value of h
	such that the given researcher has published at least h papers
	that have each been cited at least h times.

Constraints:
1. 1 <= citations.length <= 5 * 10^3
2. 0 <= citations[i] <= 10^3

Approach:
1. Find the maximum value of citation "max_citation" in citations
2. Assign an array "citation_counts" size of (max_citation + 1)
3. for each citations[i],
	citation_counts[citations[i]] += 1
4. return the index that has maximum value in it


Complexity:
1. TC = O(N)
2. SC = O(N)

*/

class Solution {
public:
	int hIndex(vector<int>& citations) {
		int n = citations.size();
		vector<int> count(n + 1, 0);
		for (int citation : citations) {
			if (citation >= n) {
				count[n] += 1;
				continue;
			}
			count[citation] += 1;
		}

		int papers = 0;
		for (int h_index = n; h_index >= 0; h_index--) {
			papers += count[h_index];

			if (papers >= h_index) {
				return h_index;
			}
		}
		return 0;
	}
};

int main()
{
	vector<int> citations;
	string line;
	getline(cin, line);

	stringstream ss(line);
	int value;
	while (ss >> value) {
		citations.push_back(value);
	}

	Solution s;
	int h_index = s.hIndex(citations);
	cout << h_index << endl;

	return 0;
}
