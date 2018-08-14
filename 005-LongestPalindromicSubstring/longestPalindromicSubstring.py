#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_s = s[::-1]

        i = 0
        longest = ""
        tmp = ""
        while i < len(s):
            if s[i] == reversed_s[i]:
                tmp += s[i]
            else:
                if len(tmp) > len(longest):
                    longest = tmp
                    tmp = ""
            i += 1

        if len(tmp) > len(longest):
            longest = tmp

        if len(longest) >= 3 and longest == longest[::-1]:
            return longest

    def longestPalindromeDP(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = ""
        len_s = len(s)
        palindrom_memo = [[False] * len_s for i in range(len_s)]
        print(palindrom_memo)
        i = 0
        while i < len_s-1:
            for j in range(0, len_s-2):
                k = j+i+1

                print(j, i, k)
                if palindrom_memo[j+1][k-1] and s[j] == s[k]:
                    palindrom_memo[j][k] = True

                    tmp = s[j:k]
                    if len(tmp) > len(longest):
                        longest = tmp
                else:
                    sub = s[j:k]
                    if sub == sub[::-1]:
                        palindrom_memo[j][k] = True

                        tmp = s[j:k]
                        if len(tmp) > len(longest):
                            longest = tmp

            i += 1

        return longest


def main():
    s = Solution()
    # print(s.longestPalindrome("aba"))
    print(s.longestPalindromeDP("aba"))


if __name__ == '__main__':
    main()
