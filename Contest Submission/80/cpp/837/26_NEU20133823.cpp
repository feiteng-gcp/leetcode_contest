class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        string ans="";
	int cnt=0;
	map<string,int> m;
	int n=banned.size();
	for(int i=0;i<n;i++)
	{
		m[banned[i]]=-1;
	}
	int len=paragraph.size();
	string now="";
	for(int i=0;i<len;i++)
	{
		char c=paragraph[i];
		if(!((c>='a'&&c<='z')||(c>='A'&&c<='Z')))
		{
			if(now=="")continue;
			if(m[now]==-1)
			{
				now="";
				continue;
			}
			if(m[now]==0)m[now]=1;
			else m[now]++;
			if(m[now]>cnt)
			{
				cnt=m[now];
				ans=now;
			}
			//cout<<now<<m[now]<<endl;
			now="";
		}
		else
		{
			if(c>='A'&&c<='Z')c=c-'A'+'a';
			now=now+c;
		}
	}
	if(now!="")
	{
		if(m[now]==0)m[now]=1;
		else m[now]++;
		if(m[now]>cnt)
		{
			cnt=m[now];
			ans=now;
		}
	}
	return ans;
    }
};