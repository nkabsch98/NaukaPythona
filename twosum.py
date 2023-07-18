#This is my solution of https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
        answer = []
        for position, number in enumerate(nums):
            if target - number in nums:
                gap = target - number
                if gap == number:
                    if nums.count(gap) != 1:
                        answer.append(position)
                else:
                     answer.append(position)
        return answer


print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))