
typedef pair<int,int> pii;

const int M1 = 32, M2 = 30000;
class Solution {
public:
    int O1 = 16;
    int O2 = 10000;

    pair<int, int> P(int a, int b) {
        int p = a - O1;
        int s = 0;
        if (a < O1) {
            p = -p - 1;
            s = 1 << p;
            s = -s;
        } else {
            s = 1 << p;
        }

        return pii(s, b - O2);
    }

    pair<int, int> D(int a, int b) {
        int pos = b + O2;
        if (a > 0) {
            int p = 0;
            while (a != 1) {
                p++;
                a = a >> 1;
            }

            return pii(p + O1, pos);
        } else {
            int p = 0;
            a = -a;
            while (a != 1) {
                p++;
                a = a >> 1;
            }

            return pii(O1-1-p, pos);
        }
    }

    int racecar(int target) {
		char dist[M1][M2];
        memset(dist, 0xff, sizeof(dist));
        dist[O1][O2] = 0;
        queue<pair<int,int> > q;
        q.push(pii(O1, O2));

        int ans;
int iter = 0;
        while (true) {
            iter++;
            pii f = q.front();
            q.pop();

            int s, p;
            tie(s, p) = P(f.first, f.second);
            if (p == target) {
                ans = dist[f.first][f.second];
                break;
            }

            int d = dist[f.first][f.second];

            {
                int np = p + s;
                int ns = s * 2;

                pii nf = D(ns, np);
                if (nf.first >= 0 && nf.first < M1 && nf.second >= 0 && nf.second < M2) {
                    if (dist[nf.first][nf.second] < 0) {
                        dist[nf.first][nf.second] = d+1;
                        q.push(nf);
                    }
                } else {
                    //cout << ns << " " << np << endl;
                }
            }

            {
                int np = p;
                int ns;
                if (s < 0) {
                    ns = 1;
                } else {
                    ns = -1;
                }

                pii nf = D(ns, np);
                if (nf.first >= 0 && nf.first < M1 && nf.second >= 0 && nf.second < M2) {
                    if (dist[nf.first][nf.second] < 0) {
                        dist[nf.first][nf.second] = d+1;
                        q.push(nf);
                    }
                } else {
                    //cout << ns << " " << np << endl;
                }
            }
        }

        return ans;
    }
};

