public class Solution
{
    public int Racecar(int target)
    {
        if(target == 0)
        {
            return 0;
        }
        var all = new Queue<(int pos, int speed)>();
        var past = new HashSet<string>();
        all.Enqueue((0, 1));
        var count = 0;
        var cut = 0;
        while(true)
        {
            count++;
            var ct = all.Count;
            
            for(var i = 0; i < ct; i++)
            {
                (var pos, var speed) = all.Dequeue();
                var key = $"{pos}:{speed}";
                if(!past.Add(key) || pos < cut)
                {
                    continue;
                }
                //R
                all.Enqueue((pos, speed > 0 ? -1 : 1));
                //A
                if(pos < target)
                cut = Math.Max(cut, pos /2);
                pos += speed;
                if(pos == target)
                {
                    return count;
                }
                speed *= 2;
                all.Enqueue((pos, speed));
            }
            
        }
        return 0;
        
    }
}