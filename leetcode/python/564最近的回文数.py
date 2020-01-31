class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        s = []
        size = len(n)
        try:
            s4 = int('9'*(size-1))
        except:
            s4 = 0
        s.append(s4)
        tmp = list(n)
        if tmp[(size-1)//2]!='0':
            tmp[(size-1)//2] =  str(int(tmp[(size-1)//2])-1)
            s2 = ''.join(tmp)
            # print(s2)
            s.append(int(s2[:(size+1)//2]+s2[::-1][(size+1)//2:]))
        s.append(int(n[:(size+1)//2]+n[::-1][(size+1)//2:]))
        # print(s1)

        tmp = list(n)
        if tmp[(size-1)//2]!='9':
            tmp[(size-1)//2] =  str(int(tmp[(size-1)//2])+1)
            s3 = ''.join(tmp)
            s.append(int(s3[:(size+1)//2]+s3[::-1][(size+1)//2:]))

        # print(type(s4))
        
        s.append(int('1'+'0'*(size-1)+'1'))
        # print(s1,s2,s3,s4,s5)
        # print(s)
        n = int(n)
        l = []
        while n in s:
            s.remove(n)
        for i in s:
            l.append(abs(i-n))
        return str(s[l.index(min(l))])
        

s = Solution()
print(s.nearestPalindromic("1"))
