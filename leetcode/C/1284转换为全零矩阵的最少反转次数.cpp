#include <stdio.h>
#include <queue>
#include <vector>
#include <utility>
#include <string>
using namespace std;
class Solution {
public:
    int minFlips(vector<vector<int> >& mat) {
        queue<pair<int, vector<vector<int> > > >que;
        int steps = 0;
        que.push(make_pair(steps,mat));
        int n = mat.size();
        int m = mat[0].size();
        return bfs(n,m,steps,mat);
    }

    int bfs(int n,int m,int steps,vector<vector<int> >& mat)
    {
        vec 
    }
};
