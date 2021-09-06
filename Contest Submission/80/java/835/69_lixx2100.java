import java.util.*;
import java.util.stream.*;
import java.math.*;

public class Solution {


    public int numComponents(ListNode head, int[] G) {
        int n = 0;
        for (ListNode p = head; p != null; p = p.next) {
            n++;
        }

        int[] pos = new int[n];
        int i = 0;
        for (ListNode p = head; p != null; p = p.next) {
            pos[p.val] = i++;
        }

        int cnt = 0;
        Integer[] g = new Integer[G.length];
        for (i = 0; i < g.length; i++) {
            g[i] = G[i];
        }
        Arrays.sort(g, Comparator.comparingInt(u -> pos[u]));
        int previous = -100;
        for (i = 0; i < g.length; i++) {
            if (pos[g[i]] != previous + 1) {
                cnt++;
            }
            previous = pos[g[i]];
        }

        return cnt;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();



    }
}
