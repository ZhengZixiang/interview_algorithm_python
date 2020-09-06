# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。 
# 
#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#  
# 
#  示例 2： 
# 
#  输入：
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# 输出：[]
#  
#  Related Topics 哈希表 双指针 字符串 
#  👍 331 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not words:
            return res
        n, m, w = len(s), len(words), len(words[0])
        tot = dict()
        for word in words:
            if word in tot:
                tot[word] += 1
            else:
                tot[word] = 1

        for i in range(w):
            window = dict()
            cnt = 0
            for j in range(i, n, w):
                if j >= i + m * w:
                    word = s[j - m * w:j - (m - 1) * w]
                    window[word] = window.setdefault(word, 0) - 1
                    if window.setdefault(word, 0) < tot.setdefault(word, 0):
                        cnt -= 1
                word = s[j:j + w]
                if word in window:
                    window[word] += 1
                else:
                    window[word] = 1
                if window.setdefault(word, 0) <= tot.setdefault(word, 0):
                    cnt += 1
                if cnt == m:
                    res.append(j - (m - 1) * w)
        return res

# leetcode submit region end(Prohibit modification and deletion)
