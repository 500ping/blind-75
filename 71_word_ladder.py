import collections
from typing import Counter, List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    nei = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for i in range(len(word)):
            pattern = f"{word[:i]}*{word[i+1:]}"
            nei[pattern].append(word)

    visit = set([beginWord])
    q = collections.deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = f"{word[:j]}*{word[j+1:]}"
                for nei_word in nei[pattern]:
                    if nei_word not in visit:
                        visit.add(nei_word)
                        q.append(nei_word)
        res += 1
    return 0


beginWord = "hot"
endWord = "dog"
wordList = ["hot", "dog"]
print(ladderLength(beginWord, endWord, wordList))
