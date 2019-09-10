#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        思路： 递归，依次遍历nums数组，对元素i, 从剩下的n-1个元素中找出m个数使得元素i与这m个数的和为sum_nums / k, 再递归剩下的n-m-1个数
        时间复杂度: ?
        """
        sum_all = sum(nums)
        if k <= 0 or len(nums) < k or sum_all % k != 0:
            return False

        # 只考虑正数的情况， 可以将nums排序，先考虑比较大的元素
        # nums.sort(reverse=True)
        return self.canPartition(nums, [0]*len(nums), 0, 0, 0, k, sum_all/k)

    def canPartition(self, nums, visited, startIndex, curSum, curNum, k, target):
        # sum_all = k*target
        # sum_all - (k-1)*target = target
        if k == 1:
            return True

        # 考虑了元素为负数的情况
        # 如果元素都为正数， 这里的条件可增加 if curSum > target: return False
        # if curSum > target:
        #     return False
        if curSum == target and curNum > 0:
            return self.canPartition(nums, visited[:], 0, 0, 0, k-1, target)
        else:
            for i in range(startIndex, len(nums)):
                if visited[i] == 0:
                    visited[i] = 1
                    if self.canPartition(nums, visited[:], i+1, curSum+nums[i], curNum+1, k, target):
                        return True
                    visited[i] = 0
            return False


if __name__ == '__main__':
    s = Solution()
    s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
