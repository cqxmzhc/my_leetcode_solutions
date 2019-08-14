#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        num%2：判断最小位置的数是否是1
        num/2: 对2进制数来说这相当于是向右移位
        递归
        """
        res = []
        for i in range(num+1):
            count = 0
            while i:
                if i % 2 == 1:
                    count += 1
                i /= 2

            res.append(count)

        return res


if __name__ == '__main__':
    pass
