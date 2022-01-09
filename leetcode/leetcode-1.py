#!/usr/bin/env python3

''' leetcode 1 - 两数之和 '''


class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i in range(len(nums)):
            val = nums[i]
            if target - val in temp:
                return [i, temp[target - val]]
            temp[val] = i
    

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if i == j:
                        break
                    return [i, j]

'''
1. 暴力循环 O(n^2)
    注意排除下标相同

2. 倒排索引
    只能是 ing ，一个在 map 内，另一个不在。

    否则，诸如 [3,3] 6

    list => val_x = val_y = target => [x, y]
    
        {
            val_x: x,
            val_y: y,
        }
   
'''