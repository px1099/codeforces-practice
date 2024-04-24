#include <bits/stdc++.h>
using namespace std;


const int MODULO = 1000000007;
const int MAX_SIZE = 300001;
vector<long long> solution(MAX_SIZE, -1);
int pointer = 0;


long long calculate(int n) {
    if (solution[n] >= 0) {
        return solution[n];
    }
    if (pointer == 0) {
        solution[0] = 1;
        solution[1] = 1;
        pointer = 2;
    }
    for (int i = pointer; i <= n; i++) {
        solution[i] = (solution[i-1] + (2*i-2) * solution[i-2]) % MODULO;
    }
    if (pointer <= n) {
        pointer = n + 1;
    }
    return solution[n];
}


void solve() {
    int n; cin >> n;
    int k; cin >> k;
    int r, c;
    for (int i = 0; i < k; i++) {
        cin >> r >> c;
        if (r == c) {
            n -= 1;
        } else {
            n -= 2;
        }
    }
    cout << calculate(n) << "\n";
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
