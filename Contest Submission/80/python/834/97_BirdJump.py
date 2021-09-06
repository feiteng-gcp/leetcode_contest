class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        num=S[1:-1]
        
        Ans=[]
        
        ## Insert only ,

        for i in range(1,len(num)):
            K1,K2=num[:i],num[i:]
            
            if str(int(K1))==K1 and str(int(K2))==K2:
                Ans.append( "("+K1+', '+K2+")" )
        
        def Judge_float(K):
            if K[-1]=='0':
                return False
            if K.startswith('0'):
                if K.startswith("0."):
                    return True
                else:
                    return False
            return True
        
        ## i:Insert, j:Insert. 
        for i in range(1,len(num)):
            for j in range(i+1,len(num)):
                K1,K2=num[:i],num[i:j]+'.'+num[j:]

                if str(int(K1))==K1 and Judge_float(K2):
                    Ans.append( "("+K1+', '+K2+")" )
                    
        for i in range(1,len(num)):
            for j in range(1,i):
                K1,K2=num[:j]+'.'+num[j:i],num[i:]
                if Judge_float(K1) and str(int(K2))==K2:
                    Ans.append( "("+K1+', '+K2+")" )
                    
        for i in range(1,len(num)):
            for j in range(1,i):
                for k in range(i+1,len(num)):
                    K1,K2=num[:j]+'.'+num[j:i],num[i:k]+'.'+num[k:]
                    if Judge_float(K1) and Judge_float(K2):
                        Ans.append( "("+K1+', '+K2+")" )
        return Ans
