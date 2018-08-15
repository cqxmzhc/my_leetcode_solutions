#!/usr/bin/env python
# -*- coding: utf-8 -*-


def expandAroundCenter(s, left, right):
    l = 0
    r = 0
    len_s = len(s)
    while left >= 0 and right < len_s and s[left] == s[right]:
        l = left
        r = right

        left -= 1
        right += 1

    return r - l + 1


class Solution(object):
    def longestPalindromeDP(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        len_s = len(s)
        # whether s[j][k] is a palindrome
        palindrom_memo = [[False] * len_s for i in range(len_s)]
        # length of substring
        i = 1
        while i <= len_s:
            # start index of substring
            for j in range(0, len_s-i+1):
                # end index of substring
                k = j + i - 1
                # if s[j+1][k-1] is a palindrome and s[j] == s[k] then s[j][k] is a palindrome
                if k - j > 2 and palindrom_memo[j+1][k-1] and s[j] == s[k]:
                    import pdb
                    pdb.set_trace()
                    palindrom_memo[j][k] = True

                    tmp = s[j:k+1]
                    if len(tmp) > len(longest):
                        longest = tmp
                else:
                    sub = s[j:k+1]
                    if sub == sub[::-1]:
                        # memoization
                        palindrom_memo[j][k] = True

                        tmp = s[j:k+1]
                        if len(tmp) > len(longest):
                            longest = tmp

            i += 1

        return longest

    def longestPalindromeAroundCenter(self, s):
        if s == None or s == "":
            return ""

        len_s = len(s)
        start = 0
        end = 0
        for i in range(0, len_s):
            # the index of center number is odd;
            len1 = expandAroundCenter(s, i, i)

            # the index of center number is even
            len2 = expandAroundCenter(s, i, i+1)

            # take the maximum
            len_max = max(len1, len2)

            if len_max >= end-start+1:
                # len_max = (i-start)*2+1
                start = i - (len_max-1) / 2
                end = len_max + start - 1

        return s[start:end+1]


def main():
    s = Solution()
    print(s.longestPalindromeAroundCenter("alaal"))


if __name__ == '__main__':
    main()
