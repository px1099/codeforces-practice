#include <bits/stdc++.h>
using namespace std;


const int MAX_SIZE = 200000;
vector<bool> cards(MAX_SIZE);


void solve() {
    int n, tmp;
    int result = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cards[i] = false;
    }
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        if (cards[tmp-1]) {
            result += 1;
        } else {
            cards[tmp-1] = true;
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
