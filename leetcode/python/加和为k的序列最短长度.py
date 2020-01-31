import collections
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        p = []
        p.append(A[0])
        for x in A:
            p.append(x+p[-1])
        ans = len(A)+1
        deq = collections.deque()
        for y,p_y in enumerate(p):
            while deq and p_y <= p[deq[-1]]:
                deq.pop()

            while deq and p_y-p[deq[0]]>=K:
                ans = min(ans, y-deq.popleft())
            deq.append(y)
        if ans == len(A)+1:
            ans = -1
        return ans

so = Solution()
A = [1,2,3]
K = 4
print(so.shortestSubarray(A,K) )