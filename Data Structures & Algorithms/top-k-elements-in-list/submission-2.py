class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



        # # 出現回数カウント hashmap
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # # valueを降順で配列に格納する
        # a = []
        # for v in count.values():
        #     a.append(v)
        # a.sort(reverse=True)
        # # count hashmapのkeyとvalueを入れ替えたh hashmapを作成
        # h = {}
        # for c, d in count.items():
        #     h[d] = c

        # m = []
        # for q in a[:k]:
        #     m.append(h.get(q, 0))
        # return m

        # ## これだと出現回数が同じものに対応できなかった

