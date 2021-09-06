public class Solution {
    public string MostCommonWord(string paragraph, string[] banned) {
        paragraph = paragraph.ToLower();

        paragraph = paragraph.Replace('!', ' ');
        paragraph = paragraph.Replace('?', ' ');
        paragraph = paragraph.Replace('\'', ' ');
        paragraph = paragraph.Replace(',', ' ');
        paragraph = paragraph.Replace(';', ' ');
        paragraph = paragraph.Replace('.', ' ');

        var splited = paragraph.Split(' ');

        Dictionary<string, int> freq = new Dictionary<string, int>();

        foreach (var s in splited)
        {
            if (string.IsNullOrEmpty(s))
            {

            }
            else
            {
                if (freq.ContainsKey(s))
                    freq[s]++;
                else
                    freq[s] = 1;
            }
        }

        int max = 0;
        string m_s = null;

        foreach (var f in freq)
        {
            if (banned.Contains(f.Key))
            {
                continue;
            }
            else
            {
                if (max < f.Value)
                {
                    max = f.Value;
                    m_s = f.Key;
                }
            }
        }

        return m_s;
    }
}