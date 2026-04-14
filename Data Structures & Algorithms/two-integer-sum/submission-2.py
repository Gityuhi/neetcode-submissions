class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        






        # for i, n in enumerate(nums):
        #     hashmap[n] = i
        #     diff = target - n
        #     if diff in hashmap:
        #         return [hashmap[diff], i]
            


        # hashlist = {}
        # for i in range(len(nums)):
        #     hashlist[nums[i]] = i
        #     print(hashlist)
        # for i in range(len(nums)):
        #     v = target - nums[i]
        #     print(v)
        #     # これvalueだから失敗している
        #     k = target - v
        #     print(k)
        #     if v + k == target and v <= k:
        #         return [hashlist[v], hashlist[k]]






# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashlist = {}
#         for i in range(len(nums)):
#             hashlist[target - nums[i]] = nums[i]
#             v = hashlist.get(target - nums[i], 0)
#             s = nums[i]
#             if v in hashlist.keys() and v > s:
#                 return [nums.index(s), nums.index(v)]
#             else:
#                 return [nums.index(v), nums.index(s)]
# 考え方が惜しかった！
# 最後もk = hashlist.get(v, 0)にしてたけど、これはvのvalueをとってきているから
# vのindexをとっており失敗していた。
# 同一のキーの場合がわからず詰まる。