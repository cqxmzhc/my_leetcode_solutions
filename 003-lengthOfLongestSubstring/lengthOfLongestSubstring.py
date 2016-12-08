class Solution(object):
    #556ms
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_length = 1 if len(s) else 0
        substring_start_index = 0
        substring_end_index = 1

        for x in xrange(1, len(s)):
            tmp_length = 1
            for y in xrange(substring_start_index, substring_end_index):
                if s[x] != s[y]:
                    tmp_length += 1
                    if(tmp_length > longest_length):
                        longest_length = tmp_length
                else:
                    substring_start_index = y + 1
            substring_end_index += 1
        return longest_length

    #106ms
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_length = 1 if len(s) else 0
        tmp_length = 1
        substring_start_index = 0
        substring_end_index = 1

        for x in xrange(1, len(s)):
            if s[x] not in s[substring_start_index:substring_end_index]:
                tmp_length = substring_end_index - substring_start_index + 1
                if(tmp_length > longest_length):
                    longest_length = tmp_length
                substring_end_index += 1
            else:
                for y in xrange(substring_start_index, substring_end_index + 1):
                    if s[y] == s[x]:
                        substring_start_index = y + 1
                        substring_end_index += 1
                        break


if __name__ == '__main__':
    my_solution = Solution()
    print my_solution.lengthOfLongestSubstring("abcabcdebb")
