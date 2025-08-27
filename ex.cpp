#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;

        // Convert string to long long
        long long n = stoll(s);
        vector<long long> results;

        long long base = 10;
        for (int k = 1; k <= 18; ++k) {
            long long multiplier = 1 + base;
            if (n % multiplier == 0) {
                long long x = n / multiplier;
                results.push_back(x);
            }
            // Avoid overflow: if base gets too big, break
            if (base > 1e18 / 10) break;
            base *= 10;
        }

        if (results.empty()) {
            cout << 0 << '\n';
        } else {
            sort(results.begin(), results.end());
            cout << results.size() << '\n';
            for (long long x : results)
                cout << x << ' ';
            cout << '\n';
        }
    }
    return 0;
}
