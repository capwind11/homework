#include "iostream"
#include "queue"
#include "vector"

using namespace std;
bool cmp(pair<int,int> a,pair<int,int> b)
{
    if (a.second > b.second)
        return true;
    else
        return false;
}
int main()
{
    int times, num, maxp,c, len, pr;
    pair<int,int> *work, temp;
    queue< pair<int,int> > que;
    cin >> times;
    priority_queue < pair<int,int>,vector <pair<int,int> >,cmp> prique;
    for(int i = 0;i < times; i++){
        cin >> num >> c;
        len = 0;
        work = new pair<int,int>[num+1];
        for(int z = 0;z < num; z++){
            cin >> pr;
            work[z] = make_pair(z,pr);
            que.push(work[z]);
            prique.push(work[z]);
        }
        while (que.front().first!= c||que.front().second < prique.front.second){
             if(que.front().second < prique.front.second){
                temp = que.front();
                que.pop();
                que.push(temp);
            }
            else{
                que.pop();
                prique.pop();
                len++;
            }
        }
        cout << len+1;


    }

}


