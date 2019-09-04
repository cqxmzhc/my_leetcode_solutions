#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0

        sorted_pairs = sorted(pairs, key=lambda x: x[1])

        pre = float("-inf")
        count = 0
        # 这里不需要像LIS问题考虑以每个元素结尾的情况
        # 对于元素(a,b), (c,d), (e,f)
        # 如果b > c, 因为b < d, 对于(c, d)以后的所有元素来说,  满足条件的最优选择仍然是选择(a, b)
        for i in sorted_pairs:
            if pre < i[0]:
                count += 1
                pre = i[1]

        return count


if __name__ == '__main__':
    pass
