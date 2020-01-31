# -*- coding: utf-8 -*-
import re
class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: 
        一个强密码应满足以下所有条件：
        由至少6个，至多20个字符组成。
        至少包含一个小写字母，一个大写字母，和一个数字。
        同一字符不能连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 是可以的)。

        编写函数 strongPasswordChecker(s)，s 代表输入字符串，如果 s 已经符合强密码条件，则返回0；否则返回要将 s 修改为满足强密码条件的字符串所需要进行修改的最小步数。

        插入、删除、替换任一字符都算作一次修改。
        """
        flag = [True]*3
        n = len(s)
        mod = [0]*3
        n_modify = 0
        for uchar in s:
            if uchar >= u'\u0030' and uchar <= u'\u0039':
                flag[0] = False
            if (uchar >= u'\u0041' and uchar <= u'\u005a'):
                flag[1] = False
            if (uchar >= u'\u0061' and uchar <= u'\u007a'):
                flag[2] = False
        print(flag)
        l = 1
        if n==0:
            return 0
        pre_c = s[0]
        for i in s[1:n]:
            if pre_c == i:
                l+=1
                if l>=3 and l%3==0:
                    n_modify += 1 
            else:
                if l>=3:
                    mod[l%3]+=1
                l = 1
            pre_c = i
        if l>=3:
            mod[l%3]+=1
        print(n_modify,mod)
        miss = 0
        for i in flag:
            miss += int(i)
        print(miss)
        if (n<6):
            return max(6-n,miss)
        if (n<=20):
            return max(n_modify,miss)
        n_remove = n-20
        if n_remove<mod[0]:
            return max(n_modify-n_remove,miss)+n-20
        n_remove-=mod[0]
        n_modify-=mod[0]
        if n_remove<mod[1]*2:
            return max(n_modify-n_remove//2,miss)+n-20
        n_remove -= mod[1]*2
        n_modify -= mod[1]
        return max(n_modify-n_remove//3,miss)+n-20



s = Solution()
ans = s.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa")
print(ans)