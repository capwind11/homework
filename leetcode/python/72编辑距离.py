class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        record =[[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1+1):
            for j in range(0,len2+1):
                if i == 0:
                    record[i][j] = j
                elif j == 0:
                    record[i][j] = i                 
                elif word1[i-1]==word2[j-1]:
                    record[i][j] = record[i-1][j-1]
                else:
                    record[i][j] = min(min(record[i-1][j],record[i][j-1]),record[i-1][j-1])+1
        # print(record)
        return record[len1][len2]

s = Solution()
n = s.minDistance('1223','111')
print(n)
# [[0, 1, 2, 3],
#  [0, 0, 1, 2], 
#  [0, 0, 1, 2], 
#  [0, 0, 0, 1], 
#  [0, 0, 0, 0]]