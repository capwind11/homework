class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        comb = []
        n = len(words)
        m = len(letters)
        step = 0
        t = ''
        self.all_comb(comb,n,step,t)
        fesiable = []
        for t in comb:
            used = [False]*m
            f = True
            for i in range(n):
                if t[i] == '0':
                    continue
                else:
                    word = list(words[i])
                    for j in range(m):
                        if letters[j] in word and not used[j]:
                            word.remove(letters[j])
                            used[j] = True
                    if len(word)!=0:
                        f = False
                        break
            if f:
                fesiable.append(t)
        max_score = 0
        table = [self.get_score(score,word) for word in words]
        for i in fesiable:
            sc = 0
            for j in range(n):
                if i[j] == '1':
                    sc += table[j]
            # print(i,sc)
            if sc > max_score:
                max_score = sc
        return max_score
                
    
    def get_score(self,score,word):
        sum = 0
        for i in word:
            sum += score[ord(i)-ord('a')]
        return sum

    def all_comb(self,comb,len,n,t):
        if n == len:
            comb.append(t)
            return
        for i in ['0','1']:
            t += i
            self.all_comb(comb,len,n+1,t)
            t = t[:-1]


s = Solution()
words = ["xxxz","ax","bx","cx"]
letters = ["z","a","b","c","x","x","x"]
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# words = ["dog","cat","dad","good"]
# letters = ["a","a","c","d","d","d","g","o","o"]
# score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# s.get_score(score,'abc')
print(s.maxScoreWords(words,letters,score))