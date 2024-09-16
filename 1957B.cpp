//go:build ignore
#include <bits/stdc++.h>
using namespace std;


void solve() {
    int n; cin >> n;
    int k; cin >> k;
    if (n == 1) {
        cout << k << "\n";
        return;
    }
    int p = 0;
    while (k >= (p+1)*2-1) {
        p = (p+1)*2-1;
    }
    cout << p << " " << k-p;
    for (int i = 0; i < n-2; i++) {
        cout << " " << 0;
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
