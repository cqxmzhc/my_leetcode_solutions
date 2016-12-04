class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)

        index_list = range(0, nums_len)
        nums_dict = {k: v for k, v in zip(nums, index_list)}

        for i, v in enumerate(nums):
            complement = target - v
            if complement in nums_dict and nums_dict[complement] != i:
                return [i, nums_dict[complement]]
