class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  # {number: index}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return [] # Should not be reached given the problem constraints (exactly one solution)

# Test Cases
print(f"Two Sum [2,7,11,15], target=9: {Solution().twoSum([2,7,11,15], 9)}") # Expected: [0, 1]
print(f"Two Sum [3,2,4], target=6: {Solution().twoSum([3,2,4], 6)}") # Expected: [1, 2]
print(f"Two Sum [3,3], target=6: {Solution().twoSum([3,3], 6)}") # Expected: [0, 1]