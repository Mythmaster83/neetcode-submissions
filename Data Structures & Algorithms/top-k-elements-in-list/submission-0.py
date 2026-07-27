from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        an = Counter(nums)

        return [num for num, freq in an.most_common(k)]
