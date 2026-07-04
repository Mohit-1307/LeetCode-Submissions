class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        patterns = defaultdict(list)

        for word in wordList:
            for i in range(L):
                patterns[word[:i] + "*" + word[i + 1:]].append(word)

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1:]

                for nxt in patterns[pattern]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))

                # avoid revisiting same bucket
                patterns[pattern] = []

        return 0