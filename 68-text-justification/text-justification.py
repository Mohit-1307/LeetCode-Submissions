class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)

        i = 0

        while i < n:
            # Find words belonging to current line
            line_len = len(words[i])
            j = i + 1

            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            num_words = j - i

            # Last line OR single-word line
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                total_chars = sum(len(word) for word in words[i:j])

                total_spaces = maxWidth - total_chars
                gaps = num_words - 1

                base = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]

                    spaces = base
                    if k - i < extra:
                        spaces += 1

                    line += " " * spaces

                line += words[j - 1]

            res.append(line)
            i = j

        return res