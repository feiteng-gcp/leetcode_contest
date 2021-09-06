/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func numComponents(head *ListNode, G []int) int {
    has := make(map[int]bool)
    for _, v := range G {
        has[v] = true
    }
    
    cnt := 0
    going := false
    for head != nil {
        if has[head.Val] {
            if !going {
                going = true
                cnt++
            }
        } else {
            if going {
                going = false
            }
        }
        head = head.Next
    }
    return cnt
}