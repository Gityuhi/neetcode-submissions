class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
                
        for s in strs:
            count = [0] * 26
            for c in s:
                # 出現回数を記録
                # c = "a"ならidx0を指して、1を追加する
                # ordはASCIIコードに変換する関数
                count[ord(c) - ord("a")] += 1
                # keyに変更可能なlistは登録できないので、変更不可のタプルに置き換える
            res[tuple(count)].append(s)
        return list(res.values())


# defaultdict, ord, tupleの扱い方を復習する