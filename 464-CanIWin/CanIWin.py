#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        全局状态state
        """
        if desiredTotal <= 0 return True
        sum_all = (1+maxChoosableInteger) * maxChoosableInteger / 2
        if sum_all < desiredTotal:
            return False

        state = [0 for _ range(maxChoosableInteger+1)]
        hash_map = {}
        return self.helper(desiredTotal, state, hash_map)

    def helper(self, desiredTotal, state, hashMap):
        cur = str(state)
        if cur in hashMap return hashMap[cur]
        for i in range(1, len(state)+1):
            # 未使用
            if state[i] == 0:
                state[i] = 1
                if desiredTotal <= i or not self.helper(desiredTotal-i, state, hashMap):
                    hashMap[cur] = True
                    state[i] = 0
                    return True
                state[i] = 0

        hashMap[cur] = False
        return False


if __name__ == '__main__':
    pass
