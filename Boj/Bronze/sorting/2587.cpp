#include <iostream>
#include <vector>

using namespace std;

void swap(int& a, int& b){
    int temp = a;
    a = b;
    b = temp;
}

void shaker_sort(int n, vector<int>& numbers){
    // TC = O(N^2)
    // SC = O(1)

    int left = 0;
    int right = n-1;
    int last = right;

    while (left < right) {

        for (int i = right; i>left; i--){
            if (numbers[i] < numbers[i-1]){
                swap(numbers[i], numbers[i-1]);
                last = i;
            }
        }
        left = last;

        for (int i = left; i < right; i++){
            if (numbers[i] > numbers[i+1]){
                swap(numbers[i], numbers[i+1]);
                last = i;
            }
        }
        right = last;

    }
}

int get_avg(vector<int>& numbers){
    int avg = 0;

    for (int i=0; i<numbers.size(); i++){
        avg += numbers[i];
    }

    return avg / numbers.size();
}


int main() {
    /*
    Problem:
    Five natural numbers is given for each line.
    1. Print the average of numbers
    2. Print the median of numbers

    Constraints:
    1. Time Limit = 1000ms
    2. Space Limit = 128MB

    Approach:
    1. Sort the numbers in ascending order
    2. Get the average
    3. Get the median
    */

    int LEN_NUMBERS = 5;

    vector<int> numbers(5);
    for(int i=0; i<LEN_NUMBERS; i++){
        cin >> numbers[i];
    }

    shaker_sort(LEN_NUMBERS, numbers);
    cout << get_avg(numbers) << endl;
    cout << numbers[LEN_NUMBERS / 2] << endl;

    return 0;
}
