//go:build ignore
#include <bits/stdc++.h>
using namespace std;


int calculate_sum(int n) {
    return n * n * n - (n - 1) * n * (n + 1) / 3 + (n - 1) * n / 2;
}


void solve() {
    int n, s, m;
    cin >> n;
    m = 2 * n;
    s = calculate_sum(n);
    cout << s << " " << m << "\n";
    for (int i = n; i > 0; i--) {
        for (int c = 1; c <= 2; c++) {
            cout << c << " " << i;
            for (int j = 1; j <= n; j++) {
                cout << " " << j;
            }
            cout << "\n";
        }
    }
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
