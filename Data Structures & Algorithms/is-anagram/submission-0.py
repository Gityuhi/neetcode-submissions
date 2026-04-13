class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        if countS == countT:
            return True
        else:
            return False


            # dictionaryがhashmap
# キーにできる型には制限がある。



# 最初与えられた文字列をソートして、等しければtrue,そうでなければfalseにしようとした。
# →これはhint1の強引な解放らしい。

# ソートなしで回答できるらしい。

# hint2で文字列の並び順が重要でないという考察をした。
# でもわからなかった。
# 他にどのようにしてanagramかどうかを見分けるかが検討つかなかった

# hint3でようやく出現頻度を記録することで、互いに同じ出現頻度かを確認するという解法に辿り着いた。

# ただ、出現回数をどのようにhashmapを用いて表現するかが分からず解説動画へ
# この一つ前の問題で、keyが作成できるかどうかの判別だけだったので、key, value両方を活かすことが想像できなかった。

# 最終的には出現した文字列キーに対して、何回出てきたかをvalueに記録するhashtableをs,tそれぞれで作成し、等号で判断することで解決できた。