#define _CRT_SECURE_NO_WARNINGS 

#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstdint>

#define MAX_RC 500
#define INF UINT32_MAX

using namespace std;

struct matrix {
	int row, col;
};

unsigned int find_min_comp(int n, const vector<matrix>& matrices) {
	// TC = O(N^3)
	// SC = O(N^2)
	
	unsigned int dp[MAX_RC][MAX_RC];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			dp[i][j] = INF;
		}
	}

	for (int i = 0; i < n; i++) {
		dp[i][i] = 0;
	}

	for (int length = 2; length <= n; length++) {
		for (int start = 0; start <= n - length; start++) {
			int end = start + length - 1;

			for (int mid = start; mid < end; mid++) {
				unsigned int cost = dp[start][mid] + dp[mid + 1][end] + (1LL * matrices[start].row * matrices[mid].col * matrices[end].col);

				dp[start][end] = min(dp[start][end], cost);
			}
		}
	}


	return dp[0][n - 1];
}

int main() {
	/*
	1. This is a matrix multiplication problem.
    2. The computation of (N*M) * (M*K) = N*M*K.
    3. And it differs, according to the order of computation.
    4. For example, suppose there are A (5*3), B (3*2), C (2*6),
          (AB)*C = 90, A*(BC) = 126.
    5. Find the minimum computation.

    Constraints
    TIME 1000ms
    SPACE 256MB
    1. 1 <= N <= 5 * 10^2
    2. 1 <= r, c <= 5 * 10^2
    3. All the matrices are computable

    Corrected Approach
    1. dp[start][end] stores the minimum number of scalar multiplications
		needed to mulitply matrices[start] through matrices[end].
    2. Base case: dp[i][i] for i in range(n)
    3. Transition:
			To compute dp[start][end], try all possible positions mid between start and end - 1.
			dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid+1][end] + cost)
			cost = matrices[start].row * matrices[mid].col * matrices[end].col
	4. for length in range(2, n):
		for start in range(n-length):
			end = start + legnth - 1
			
			for mid in range(start, end):
			 cost = dp[start][mid] * dp[mid+1][end] + matrices[start].row * mtarces[mid].col * matrices[end].col
			 
			 dp[start][end] = min(dp[start][end], cost)

	5. return dp[0][n-1]

    Initial Approach, which proved to be wrong.
    1. This is a dp problem.
    2. Previous state [r][c] can multiply every [c][x] matrix into [r][x], if there's one.
    3. dp[i][r][c] = computation.
    4. dp = [[[float("inf) for _ in range(R+1)] for _ in range(C+1)] for _ in range(n+1)].
          dp[0][0] = 1
    5. By iterating a nested loop, optimal answer for each iteration is guaranteed.
    6. But with this approach, the space complexity becomes an issue.
          SC = O(500^3) = O(125 * 10^6 * 4byte) = 4MB * 125 = 500MB > 256MB
    7. Therefore, dictionary is more appropriate than using an array.
    8. dp = [defaultdict(int) for _ in range(n+1)]
    9. dp[i][r] = min(dp[i][r], dp[i-1][c] * (r*c) if dp[i-1][c])
       dp[i][c] = min(dp[i][c], dp[i-1][r] * (r*c) if dp[i-1][r])
    10. return min(dp[n])
	*/

	int n;
	vector<matrix> matrices;

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int r, c;
		scanf("%d %d", &r, &c);
		matrices.push_back({ r, c });
	}

	printf("%u\n", find_min_comp(n, matrices));

	return 0;
}