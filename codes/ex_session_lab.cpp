#include<iostream>

//using namespace std;

int main() {
    int n;
    std::cin >> n;

    int arr[n][2];

    for (int i = 0; i < n; i++) {
        long long a, b;
        std::cin >> arr[i][0] >> arr[i][1];
    }

    for (int i = 0; i < n; i++) {
        std::cout << arr[i][0] + arr[i][1] + 1 << "\n";
    }
}