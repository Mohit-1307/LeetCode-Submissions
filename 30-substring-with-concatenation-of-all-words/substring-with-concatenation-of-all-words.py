class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        target = Counter(words)
        ans = []

        for offset in range(word_len):

            left = offset
            curr_count = defaultdict(int)
            words_used = 0

            for right in range(offset,
                               len(s) - word_len + 1,
                               word_len):

                word = s[right:right + word_len]

                if word in target:

                    curr_count[word] += 1
                    words_used += 1

                    while curr_count[word] > target[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        words_used -= 1
                        left += word_len

                    if words_used == word_count:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        words_used -= 1
                        left += word_len

                else:
                    curr_count.clear()
                    words_used = 0
                    left = right + word_len

        return ans