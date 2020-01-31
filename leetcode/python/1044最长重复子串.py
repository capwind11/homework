class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        down = 1
        mod = 2**32
        up = n 
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        # print(nums)
        # print(k)
        ans = []
        while up != down:
            k = down+ (up-down)//2
            tmp = self.find_len_k(nums,k,mod)
            if len(tmp)>0:
                ans = tmp
                down = k+1
            else:
                up = k
        if len(ans)>0:
            return S[ans[0]:ans[1]]
        else:
            return ''
    
    def find_len_k(self,s,k,mod):
        sum = 0
        for j in s[0:k]:
            sum=(sum*26+j)%mod
        f={sum}
        al = pow(26,k,mod)
        for i in range(k,len(s)):
            sum = sum*26-s[i-k]*al+s[i]
            # print(s[i+1-k:i+1],sum)
            if sum in f:
                return [i-k+1,i+1]
            f.add(sum)
        return []

s = Solution()
ans = s.longestDupSubstring("ababdaebdabedeabbdddbcebaccececbccccebbcaaabaadcadccddaedaacaeddddeceedeaabbbbcbacdaeeebaabdabdbaebadcbdebaaeddcadebedeabbbcbeadbaacdebceebceeccddbeacdcecbcdbceedaeebdaeeabccccbcccbceabedaedaacdbbdbadcdbdddddcdebbcdbcabbebbeabbdccccbaaccbbcecacaebebecdcdcecdeaccccccdbbdebaaaaaaeaaeecdecedcbabedbabdedbaebeedcecebabedbceecacbdecabcebdcbecedccaeaaadbababdccedebeccecaddeabaebbeeccabeddedbeaadbcdceddceccecddbdbeeddabeddadaaaadbeedbeeeaaaeaadaebdacbdcaaabbacacccddbeaacebeeaabaadcabdbaadeaccaecbeaaabccddabbeacdecadebaecccbabeaceccaaeddedcaecddaacebcaecebebebadaceadcaccdeebbcdebcedaeaedacbeecceeebbdbdbaadeeecabdebbaaebdddeeddabcbaaebeabbbcaaeecddecbbbebecdbbbaecceeaabeeedcdecdcaeacabdcbcedcbbcaeeebaabdbaadcebbccbedbabeaddaecdbdbdccceeccaccbdcdadcccceebdabccaebcddaeeecddddacdbdbeebdabecdaeaadbadbebecbcacbbceeabbceecaabdcabebbcdecedbacbcccddcecccecbacddbeddbbbadcbdadbecceebddeacbeeabcdbbaabeabdbbbcaeeadddaeccbcdabceeabaacbeacdcbdceebeaebcceeebdcdcbeaaeeeadabbecdbadbebbecdceaeeecaaaedeceaddedbedbedbddbcbabeadddeccdaadaaeaeeadebbeabcabbdebabeedeeeccadcddaebbedadcdaebabbecedebadbdeacecdcaebcbdababcecaecbcbcdadacaebdedecaadbaaeeebcbeeedaaebbabbeeadadbacdedcbabdaabddccedbeacbecbcccdeaeeabcaeccdaaaddcdecadddabcaedccbdbbccecacbcdecbdcdcbabbeaacddaeeaabccebaaaebacebdcdcbbbdabadeebbdccabcacaacccccbadbdebecdaccabbecdabdbdaebeeadaeecbadedaebcaedeedcaacabaccbbdaccedaedddacbbbdbcaeedbcbecccdbdeddcdadacccdbcdccebdebeaeacecaaadccbbaaddbeebcbadceaebeccecabdadccddbbcbaebeaeadacaebcbbbdbcdaeadbcbdcedebabbaababaacedcbcbceaaabadbdcddadecdcebeeabaadceecaeccdeeabdbabebdcedceaeddaecedcdbccbbedbeecabaecdbba")
print(ans)
