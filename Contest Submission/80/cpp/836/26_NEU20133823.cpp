class Solution {
public:
    struct fff
{
	int p;
	int v;
	int steps;
	bool operator < (const fff &a) const
	{
		if(steps==a.steps)
		{
			if(p==a.p)return v<a.v;
			return p<a.p;
		}
		return steps>a.steps;
	}
};
    int racecar(int target) {
        priority_queue<fff> q;
	set<fff> s;
	fff st;
	st.p=0;
	st.v=1;
	st.steps=0;
	s.insert(st);
	q.push(st);
	while(!q.empty())
	{
		fff now=q.top();
		//printf("%d %d %d\n",now.p,now.v,now.steps);
		q.pop();
		fff news;
		news.steps=0;
		news.p=now.p+now.v;
		news.v=now.v+now.v;
		if(news.p>=-20000&&news.p<=20000&&news.v>=-20000&&news.v<=20000&&s.find(news)==s.end())
		{
			//printf("%d %d %d\n",news.p,news.v,news.steps);
			s.insert(news);
			news.steps=now.steps+1;
			if(news.p==target)return news.steps;
			q.push(news);
		}
		news.steps=0;
		news.p=now.p;
		if(now.v>0)news.v=-1;
		else news.v=1;
		if(s.find(news)==s.end())
		{
			//printf("%d %d %d\n",news.p,news.v,news.steps);
			s.insert(news);
			news.steps=now.steps+1;
			q.push(news);
		}
	}
	return -1;
    }
};