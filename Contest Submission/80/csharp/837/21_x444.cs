public class Solution
{
    public string MostCommonWord(string paragraph, string[] banned)
    {
        var words = new Dictionary<string, int>();
        var ban = new HashSet<string>();
        foreach(var b in banned)
        {
            ban.Add(b.ToLower());
        }
        
        var curr = "";
        
        foreach(var ch in paragraph + ' ')
        {
            if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
            {
                curr += ch;
            }
            else if(curr != "")
            {
                curr = curr.ToLower();
                if(!ban.Contains(curr))
                {
                    if(!words.ContainsKey(curr))
                    {
                        words.Add(curr, 1);
                    }
                    else
                    {
                        words[curr]++;
                    }
                }
                curr = "";
            }
        }
        
        if(words.Any())
        {
            return words.OrderByDescending(w => w.Value).First().Key;
        }
        return "";
    }
}