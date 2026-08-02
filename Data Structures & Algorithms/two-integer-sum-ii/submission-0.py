class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        minimum = 0
        maximum = len(numbers) - 1
        while maximum - minimum > 0:
            if (numbers[minimum] + numbers[maximum]) == target:
                return [minimum+1, maximum+1]
            elif (numbers[minimum] + numbers[maximum]) < target:
                minimum += 1
            else:
                maximum -= 1
        