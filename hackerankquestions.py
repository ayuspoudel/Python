class Solution:
    def buildArray(self, nums):
        list1 = []
        for i in nums:
            list1.append(nums[i])
        return list1
input_str = input()
nums1 = list(map(int, input_str.replace("[","").replace("]","").split(",")))
solution = Solution()
print(solution.buildArray(nums1))


    