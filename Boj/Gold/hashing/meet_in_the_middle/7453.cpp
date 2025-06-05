#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>
#include <unordered_map>

using namespace std;

long long find_valid_pairs(int n, const vector<int>& A, const vector<int>& B, const vector<int>& C, const vector<int>& D) {
	long long pairs = 0;
	unordered_map<int, int> sum_AB;
	sum_AB.reserve(n * n);

	for (int a : A) {
		for (int b : B) {
			sum_AB[a + b]++;
		}
	}

	for (int c : C) {
		for (int d : D) {
			int opponent = -(c + d);

			if (sum_AB.count(opponent)) {
				pairs += sum_AB[opponent];
			}
		}
	}

	return pairs;
}

int main() {
	/*
	# 1. There are four arrays A, B, C, D, which are same N long.
	# 2. Find the number of combinations(a, b, c, d),
	#       which are from A[a], B[b], C[c], D[d] that makes sum 0.

	# Constraints
	# TIME 12000ms
	# SPACE 1024MB
	# 1. 1 <= N <= 4 * 10 ^ 3
	# 2. - 2 ^ 28 <= element <= 2 ^ 28

	# Approach
	# 1. A naive nested loop would take O(N ^ 4).
	# 2. The key is to reduce the time complexity to O(N ^ 2) at most,
	#       so that it can take O(16 * 10 ^ 6).
	# 3. I thought this was a DP problem or a prefix sum at first glance,
	#       but actually it isn't, because there are no valid subproblems
	# and the time complexity does not support it.
	# 4. To make this problem only take O(N ^ 2), the four arrays has to be divided into two groups.
	# 5. It could be any combination of the followings : (A, B) / (C, D), (A, C) / (B, D), (A, D) / (B, C), ...
	#       because it will result in A + B + C + D anyway.
	# 6. So, to get the correct answer in the due time,
	#       compute all the sum of each(A, B), (C, D) pair O(N ^ 2),
	# and find if there were corresponding negative sum.O(N) with O(1) access.

	#    Incorrect
	# 7. This will take an additional space O(2 * N ^ 2) = 4byte * 2 * (4 * 10 ^ 3) ^ 2 = (8 * 16)MB = 128MB < 1024MB.

	# 8. Hash table is essential to achieve O(N ^ 2) complexity,
	#       because(N ^ 2) array iteration will take O(N ^ 3) even if it got flattened.
	# 9. AB = defaultdict[int]
	#       for a in A :
	#           for b in B :
	#               AB[a + b] += 1
	# 10. for c in C :
	#       for d in D :
	#           opponent = c + d
	#               if AB[-oppoenent]:
	#                   count += AB[-opponent]
	*/

	int n;
	scanf("%d", &n);

	vector<int> A, B, C, D;
	for (int i = 0; i < n; i++) {
		int a, b, c, d;
		scanf("%d %d %d %d", &a, &b, &c, &d);
		A.push_back(a);
		B.push_back(b);
		C.push_back(c);
		D.push_back(d);
	}

	printf("%lld", find_valid_pairs(n, A, B, C, D));

	return 0;
}