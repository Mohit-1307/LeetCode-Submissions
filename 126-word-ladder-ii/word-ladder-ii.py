class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)

        if endWord not in words:
            return []

        parents = defaultdict(list)

        dist = {beginWord: 0}

        q = deque([beginWord])

        L = len(beginWord)

        while q:
            word = q.popleft()

            if word == endWord:
                continue

            step = dist[word]

            word_chars = list(word)

            for i in range(L):
                original = word_chars[i]

                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original:
                        continue

                    word_chars[i] = c
                    nxt = "".join(word_chars)

                    if nxt not in words:
                        continue

                    # first time seen
                    if nxt not in dist:
                        dist[nxt] = step + 1
                        parents[nxt].append(word)
                        q.append(nxt)

                    # another shortest parent
                    elif dist[nxt] == step + 1:
                        parents[nxt].append(word)

                word_chars[i] = original

        if endWord not in dist:
            return []

        ans = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)
        return ans