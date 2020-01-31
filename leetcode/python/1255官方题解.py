import collections
class Solution:
    def maxScoreWords(self, words, letters, score):
        def dfs(i, n, cur_letters,table):
            if i == n:
                return 0

            ret = dfs(i + 1, n, cur_letters,table)
            ith_letter = collections.Counter(words[i])
            check = all(cur_letters[k] >= v for k, v in ith_letter.items())
            if check:
                ith_score = table[i]
                cur_letters -= ith_letter
                ret = max(ret, ith_score + dfs(i + 1, n, cur_letters,table))
                cur_letters += ith_letter
            return ret

        n = len(words)
        table = [sum(score[ord(k) - ord('a')]  for k in word) for word in words ]
        # print(table)
        c_letters = collections.Counter(letters)
        return dfs(0, n, c_letters,table)

s = Solution()
words = ["xxxz","ax","bx","cx"]
letters = ["z","a","b","c","x","x","x"]
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# words = ["dog","cat","dad","good"]
# letters = ["a","a","c","d","d","d","g","o","o"]
# score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# s.get_score(score,'abc')
print(s.maxScoreWords(words,letters,score))