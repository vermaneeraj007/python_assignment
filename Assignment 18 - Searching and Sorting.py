



#Answer ------ 1



def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start times
    merged = []

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged_intervals = merge_intervals(intervals)
print(merged_intervals)






#Answer ------ 2



def sortColors(nums):
    left, curr = 0, 0
    right = len(nums) - 1

    while curr <= right:
        if nums[curr] == 0:
            nums[left], nums[curr] = nums[curr], nums[left]
            left += 1
            curr += 1
        elif nums[curr] == 1:
            curr += 1
        else:
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1

    return nums
nums1 = [2, 0, 2, 1, 1, 0]
sorted_nums1 = sortColors(nums1)
print(sorted_nums1)

nums2 = [2, 0, 1]
sorted_nums2 = sortColors(nums2)
print(sorted_nums2)







#Answer ------ 4


def maximumGap(nums):
    if len(nums) < 2:
        return 0
    
    # Find the maximum element in nums
    maxNum = max(nums)
    
    # Perform radix sort
    exp = 1
    while maxNum // exp > 0:
        nums = countingSort(nums, exp)
        exp *= 10
    
    # Calculate the maximum difference
    maxDiff = 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        maxDiff = max(maxDiff, diff)
    
    return maxDiff

def countingSort(nums, exp):
    n = len(nums)
    count = [0] * 10
    output = [0] * n
    
    for num in nums:
        digit = (num // exp) % 10
        count[digit] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        digit = (nums[i] // exp) % 10
        output[count[digit] - 1] = nums[i]
        count[digit] -= 1
    
    return output
# Example 1
nums1 = [3, 6, 9, 1]
max_diff1 = maximumGap(nums1)
print(max_diff1)

# Example 2
nums2 = [10]
max_diff2 = maximumGap(nums2)
print(max_diff2)




#Answer ------ 5


def containsDuplicate(nums):
    numSet = set()
    for num in nums:
        if num in numSet:
            return True
        numSet.add(num)
    return False
# Example 1
nums1 = [1, 2, 3, 1]
print(containsDuplicate(nums1))  # Output: True

# Example 2
nums2 = [1, 2, 3, 4]
print(containsDuplicate(nums2))  # Output: False

# Example 3
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums3))  # Output: True








#Answer ------ 6



def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])  # Sort balloons based on end points

    arrowCount = 1
    maxEnd = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > maxEnd:
            # Need a new arrow, increment count and update maxEnd
            arrowCount += 1
            maxEnd = points[i][1]
        # If points[i][0] <= maxEnd, no additional arrow is required

    return arrowCount
# Example 1
points1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(findMinArrowShots(points1))  # Output: 2

# Example 2
points2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(findMinArrowShots(points2))  # Output: 4

# Example 3
points3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(findMinArrowShots(points3))  # Output: 2





#Answer ------ 7

def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Initialize dp array with 1

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Length of the longest increasing subsequence


# Testing the function with the given examples
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums1))  # Output: 4

nums2 = [0, 1, 0, 3, 2, 3]
print(lengthOfLIS(nums2))  # Output: 4

nums3 = [7, 7, 7, 7, 7, 7, 7]
print(lengthOfLIS(nums3))  # Output: 1






#Answer ------ 8


def find132pattern(nums):
    stack = []
    s2 = float('-inf')
    n = float('-inf')

    for num in reversed(nums):
        if num > s2:
            return True

        while stack and num > stack[-1]:
            s2 = max(s2, stack.pop())

        stack.append(num)
        if num > n:
            n = num

    return False

nums1 = [1, 2, 3, 4]
print(find132pattern(nums1))  # Output: False

nums2 = [3, 1, 4, 2]
print(find132pattern(nums2))  # Output: True

nums3 = [-1, 3, 2, 0]
print(find132pattern(nums3))  # Output: True



