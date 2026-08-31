class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in closedToOpen:
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


        


## 初見でわからなかったこと
### 質問したいこと
# ・correct orderとは"([{}])"のようにopenとclosedの順番が対応しているという理解であっているか
# ・"()[]"はfalseか→Trueだった

### 解き方の不明点
# openとclosedが対応しているhashmapを作って、twopointerで挟み込んで評価していく。
# 制約が1000あるから、最大500回評価が必要になる。hashmap分のメモリが必要になる。
# 以下のようにhashmapとopen, closedを対応させてtwopointerで評価したが、"(){}[]"がTrueになるので難しい
# 左右対称のものしか判定できない

        # bracket_map = {"(": ")", "{": "}", "[": "]"}
        # start, end = 0, len(s) - 1
        # for i in range(len(s) // 2):
        #     if bracket_map[s[start]] == s[end]:
        #         start += 1
        #         end -= 1
        #     else:
        #         return False
        # return True

## stackの使い方と書き方わかれば解ける