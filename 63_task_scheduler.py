from collections import Counter, deque
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    """
    Formual: total time intervals = (max_freq_element - 1) * (n + 1) + (all elements with max freq)
    """
    freq = list(Counter(tasks).values())
    maxFreq = max(freq)
    maxFreqCount = freq.count(maxFreq) # total_elements_with_max_freq, last row elements
        
    ans = (maxFreq - 1) * (n+1) + maxFreqCount
    
    return max(ans, len(tasks))


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

print(leastInterval(tasks, n))