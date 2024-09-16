//go:build ignore
#include <bits/stdc++.h>
using namespace std;


void solve() {
    int n; cin >> n;
    int result = 0;
    int tmp;
    map<int, int> sticks;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        sticks[tmp] = sticks[tmp] + 1;
        if (sticks[tmp] % 3 == 0) {
            result += 1;
        }
    }
    cout << result << "\n";
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
