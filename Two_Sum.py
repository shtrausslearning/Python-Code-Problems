class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            rem = target - nums[i]  # remaining value
            if rem in d:            # remaining value found
                return [d[rem],i]   # returning the value present at  key with the current index
            else:
                d[nums[i]] = i    # updating the dict. with key as number as value as index
        
Solution().twoSum(nums=[2,8,11,15],target = 11)
