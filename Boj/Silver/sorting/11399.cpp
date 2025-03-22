#include <iostream>
#include <vector>

using namespace std;

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;

}

vector<int> sort(int n, vector<int> people) {
    for (int i=0; i < n - 1; i++) {
        bool swapped = false;

        for (int j=0; j < n - 1 - i; j++) {
            if (people[j] > people[j+1]) {
                swap(&people[j], &people[j+1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return people;
}

int main() {
    // TC = O(N^2)
    // SC = O(N)

    /*
    Problem:
    With N people waiting in a line,
    each one has their own task time(1 <= P <= 1000).
    The total time each one spend is defined as sum of waiting time + task time
    Find the minimum total time spent.

    Constraints:
    1. 1 <= N <= 1000
    2. 1 <= Pi <= 1000
    3. Time <= 1000ms (10^8)
    4. Space <= 256mb (2^8*2^10*2^10)

    Approach:
    1. Sort the task time in ascending order.
    2. Given the constraints, O(1000^2) is within the limit
    */

    int n;
    cin >> n;

    vector<int> people(n);
    for (int i = 0; i < n; i++) {
        cin >> people[i];
    }

    vector<int> sorted = sort(n, people);

    int wait_time = 0;
    int total_time = 0;
    for (int i=0; i<n; i++) {
        wait_time += sorted[i];
        total_time += wait_time;
    }

    cout << total_time << endl;

    return 0;
}
