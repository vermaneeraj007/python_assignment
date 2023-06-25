


        #Answer -------- 1


def firstUniqChar(s):
    char_counts = {}
    
    # Count the occurrences of each character
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # Find the first non-repeating character and return its index
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i
    
    # If no non-repeating character found, return -1
    return -1



print(firstUniqChar("leetcode"))       # Output: 0
print(firstUniqChar("loveleetcode"))   # Output: 2



                 #Answer -------- 2



def maxSubarraySumCircular(nums):
    def kadane(nums):
        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    max_sum_case1 = kadane(nums)
    total_sum = sum(nums)
    
    # Negate the elements of the array
    negated_nums = [-num for num in nums]
    
    # Find the minimum sum subarray (maximum sum of negated subarray)
    min_sum_case2 = kadane(negated_nums)
    
    # Calculate the maximum sum wrapping around
    max_sum_case2 = total_sum + min_sum_case2
    
    # Return the maximum of case 1 and case 2
    return max(max_sum_case1, max_sum_case2) if max_sum_case1 > 0 else max_sum_case1


print(maxSubarraySumCircular([1, -2, 3, -2]))
print(maxSubarraySumCircular([5, -3, 5]))       



                 #Answer -------- 3


def countStudents(students, sandwiches):
    count = 0  # Number of students who are unable to eat

    while students:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            count = 0  # Reset the count since a student was able to eat
        else:
            students.append(students.pop(0))
            count += 1

        # Check if all remaining students are unable to eat
        if count == len(students):
            break

    return count



students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
print(countStudents(students, sandwiches))  # Output: 0

students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
print(countStudents(students, sandwiches))  # Output: 3







                 #Answer -------- 4


from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Add the new request to the end of the queue
        self.requests.append(t)
        
        # Remove requests outside the time range
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the number of requests within the time frame
        return len(self.requests)

recentCounter = RecentCounter()
print(recentCounter.ping(1))     # Output: 1
print(recentCounter.ping(100))   # Output: 2
print(recentCounter.ping(3001))  # Output: 3
print(recentCounter.ping(3002))  # Output: 3








                 #Answer -------- 5


def findTheWinner(n, k):
    friends = list(range(1, n + 1))
    index = 0

    while len(friends) > 1:
        index = (index + k - 1) % len(friends)
        friends.pop(index)

    return friends[0]
n = 5
k = 2
print(findTheWinner(n, k))  # Output: 3

n = 6
k = 5
print(findTheWinner(n, k))  # Output: 1




                 #Answer -------- 6



from collections import deque
import heapq

def deckRevealedIncreasing(deck):
    deck.sort()  # Sort the deck in ascending order
    result = deque()  # Result list to store revealed cards

    # Iterate through the sorted deck in reverse order
    for i in range(len(deck) - 1, -1, -1):
        if result:
            # Move the last card to the beginning by placing it at the bottom
            result.appendleft(result.pop())

        # Take the top card from the deck and reveal it
        result.appendleft(deck[i])

    return list(result)
deck = [1, 1000]
print(deckRevealedIncreasing(deck))  # Output: [1, 1000]







                 #Answer -------- 7



from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.front = deque()
        self.back = deque()

    def pushFront(self, val):
        self.front.appendleft(val)

    def pushMiddle(self, val):
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)

    def pushBack(self, val):
        self.back.append(val)

    def popFront(self):
        if self.front:
            return self.front.pop()
        elif self.back:
            self.front.append(self.back.popleft())
            return self.front.pop()
        else:
            return -1

    def popMiddle(self):
        if len(self.front) > len(self.back):
            return self.front.pop()
        else:
            return self.back.popleft()

    def popBack(self):
        if self.back:
            return self.back.pop()
        elif self.front:
            self.back.append(self.front.pop())
            return self.back.pop()
        else:
            return -1
q = FrontMiddleBackQueue()
print(q.popFront())  # Output: -1
q.pushFront(1)
q.pushBack(2)
q.pushMiddle(3)
q.pushMiddle(4)
print(q.popFront())  # Output: 1
print(q.popMiddle())  # Output: 3
print(q.popMiddle())  # Output: 4
print(q.popBack())  # Output: 2
print(q.pop())





                 #Answer -------- 8


from collections import deque

class DataStream:
    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.stream = deque()

    def consec(self, num):
        self.stream.append(num)
        if len(self.stream) > self.k:
            self.stream.popleft()
        return len(self.stream) == self.k and all(x == self.value for x in self.stream)
dataStream = DataStream(4, 3)
print(dataStream.consec(4))  # Output: False
print(dataStream.consec(4))  # Output: False
print(dataStream.consec(4))  # Output: True
print(dataStream.consec(3))  # Output: False



      
