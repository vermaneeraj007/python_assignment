


#Answer ----------- 1


import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    minHeap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(minHeap, (lst.val, i, lst))

    dummy = ListNode()
    current = dummy

    while minHeap:
        _, index, node = heapq.heappop(minHeap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(minHeap, (node.next.val, index, node.next))

    return dummy.next


# Example 1
lists1 = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]
result1 = mergeKLists(lists1)
while result1:
    print(result1.val, end=" ")
    result1 = result1.next
# Output: 1 1 2 3 4 4 5 6

# Example 2
lists2 = []
result2 = mergeKLists(lists2)
print(result2)
# Output: None

# Example 3
lists3 = [[]]
result3 = mergeKLists(lists3)
print(result3)
# Output: None





#Answer -------- 2

def countSmaller(nums):
    def merge_and_count(nums, start, mid, end, sorted_nums, count):
        i, j, k = start, mid + 1, start
        smaller_count = 0
        while i <= mid and j <= end:
            if nums[i] > nums[j]:
                smaller_count += mid - i + 1
                sorted_nums[k] = nums[j]
                j += 1
            else:
                sorted_nums[k] = nums[i]
                i += 1
            k += 1

        while i <= mid:
            sorted_nums[k] = nums[i]
            i += 1
            k += 1

        while j <= end:
            sorted_nums[k] = nums[j]
            j += 1
            k += 1





#Answer -------- 3



def merge_sort(nums, start, end):
    if start >= end:
        return
    
    mid = (start + end) // 2
    merge_sort(nums, start, mid)
    merge_sort(nums, mid + 1, end)

    i, j, k = start, mid + 1, start
    sorted_nums = [0] * (end - start + 1)

    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            sorted_nums[k - start] = nums[i]
            i += 1
        else:
            sorted_nums[k - start] = nums[j]
            j += 1
        k += 1

    while i <= mid:
        sorted_nums[k - start] = nums[i]
        i += 1
        k += 1

    while j <= end:
        sorted_nums[k - start] = nums[j]
        j += 1
        k += 1

    nums[start:end+1] = sorted_nums

def sortArray(nums):
    merge_sort(nums, 0, len(nums) - 1)
    return nums



#Answer -------- 4



def moveZeroes(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] != 0:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1

    return nums
nums = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
print(moveZeroes(nums))  # Output: [1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0]








#Answer -------- 5

def alternatePositiveNegative(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] > 0:
            left += 1
        elif nums[right] < 0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums
nums = [1, 2, 3, -4, -1, 4]
print(alternatePositiveNegative(nums))  # Output: [-4, 1, -1, 2, 3, 4]

nums = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(alternatePositiveNegative(nums))  # Output: [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]







#Answer -------- 6




def mergeSortedArrays(arr1, arr2):
    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged
arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
print(mergeSortedArrays(arr1, arr2))  # Output: [1, 2, 3, 4, 4, 5, 6, 8]

arr1 = [5, 8, 9]
arr2 = [4, 7, 8]
print(mergeSortedArrays(arr1, arr2))  # Output: [4, 5, 7, 8, 8, 9]






#Answer -------- 7

def intersection(nums1, nums2):
    set1 = set(nums1)
    intersection = set()

    for num in nums2:
        if num in set1:
            intersection.add(num)

    return list(intersection)
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))  # Output: [2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))  # Output: [9, 4]






#Answer -------- 8

def intersect(nums1, nums2):
    freqMap = {}
    
    for num in nums1:
        if num in freqMap:
            freqMap[num] += 1
        else:
            freqMap[num] = 1
    
    intersection = []
    
    for num in nums2:
        if num in freqMap and freqMap[num] > 0:
            intersection.append(num)
            freqMap[num] -= 1
    
    return intersection
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # Output: [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))  # Output: [4, 9]



