#!/usr/bin/env python3

''' leetcode 242 - 有效的字母异位词 '''

class Solution:
    def isAnagram_1(self s: str, t: str) -> bool:
        return sorted(s) == sorted(t) 

    def isAnagram_2(self, s: str, t:str) -> bool:
        if len(s) != len(t):
            return False

        dict_1, dict_2 = {}, {}      
        for item in s:
            dict_1[item] = dict_1.get(item, 0) + 1
        for item in t:
            dict_2[item] = dict_2.get(item, 0) + 1
        
        return dict_1 == dict_2

    def isAnagram_3(self s: str, t: str) -> bool:
        arr_1, arr_2 = [0]*26, [0]*26
        for item in s:
            arr_1[ord(item) - ord('a')] += 1
        for item in t:
            arr_2[ord(item) - ord('a')] += 1
        
        return arr_1 == arr_2


'''
keywords： 若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词

1. sort 快排 O(nlogn)
2. dict 计数 O(n)
    map、hash_function 
'''
