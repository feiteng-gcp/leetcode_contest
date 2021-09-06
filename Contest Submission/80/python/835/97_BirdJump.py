# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        Value=[]
        P=head
        while(P):
            Value.append(P.val)
            P=P.next
    
        Ans=0
        
        SG=set(G)
        
        Start=-1
        for i in range(0,len(Value)):
            if Value[i] in SG:
                if Start==-1:
                    Start=1
            else:
                if Start==1:
                    Ans+=1
                    Start=-1
        if Start==1:
            Ans+=1
        return Ans
        