#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>

using namespace std;

/*
Problem:
1. For given number of triangles, N,
2. P(N) represents the length of the hypotenuse
3. Find P(N)

Constraints:
TIME 1000ms
SPACE 128MB
1. 1 <= N <= 100

Approach:
1. This forms a padovan sequence.
2. The sequence is: 1, 1, 2, 2, 3, 4, 5, 7, ...
3. The recurrence relation is: P(n) = P(n-1) + P(n-5) for n > 5

Total Complexity:
1. TC = O(N)
2. SC = O(N)

*/

class Solution {
private:
	int t;
	vector<unsigned long long> sequence = { 0,1,1,1,2,2 };

	void generate_sequence(int n) {

		for (int i = 6; i <= n; i++) {
			sequence.push_back(sequence[i - 1] + sequence[i - 5]);
		}

	}

public:
	Solution() {
		scanf("%d", &t);
	}

	void print_length() {
		int max_n = 0;
		vector<int> test_cases(t);
		
		for (int i = 0; i < t; i++) {
			scanf("%d", &test_cases[i]);
			max_n = max(max_n, test_cases[i]);
		}

		generate_sequence(max_n);


		for (int n : test_cases) {
			printf("%llu\n", sequence[n]);
		}
	}
};

int main()
{
	Solution s;
	s.print_length();

	return 0;
}