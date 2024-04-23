#include <bits/stdc++.h>
using namespace std;


void solve() {
    int k, q, n;
    cin >> k >> q;
    vector<int> a(k);
    for (int j = 0; j < k; j++) {
        cin >> a[j];
    }
    for (int i = 0; i < q; i++) {
        if (i > 0) {
            cout << " ";
        }
        cin >> n;
        for (int j = k-1; j >= 0; j--) {
            if (n < a[j]) {
                continue;
            }
            n = n - ((n - a[j]) / (j + 1) + 1) * (j + 1);
        }
        cout << n;
    }
    cout << "\n";
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
