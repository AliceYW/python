# message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]
# def reverse_words(message):
#
#     def reverse(i, j):
#         while i < j:
#             message[i], message[j] = message[j], message[i]
#             i += 1
#             j -= 1
#
#     def word_end(i):
#         while i < len(message) and message[i] != ' ':
#             i += 1
#         return i
#
#     start = 0
#
#     while start < len(message):
#         end = word_end(start)
#         reverse(start, end-1)
#         start = end + 1
#         print(message)
#     reverse(0, len(message)-1)
#
#
# print(message)
# reverse_words(message)
# print(message)
# import bisect
# def insert(intervals,new_interval):
#     start, end = new_interval
#     start_idx = bisect.bisect_left([v[1] for v in intervals], start)
#     end_idx = bisect.([v[0] for v in intervals], end)-1
#
#     start = min(start, intervals[start_idx][0])
#     end = max(end, intervals[end_idx][1])
#
#     return intervals[:start_idx] + [[start,end]] + intervals[end_idx+1:]
#
#
#
# print(insert([[1,3], [5,7], [8,12]],[4,6]))
# def find_missing_number(nums):
#     # total = len(nums) * (len(nums) + 1) // 2
#     # return total - sum(nums)
#
#     nums.append('?')
#     print(nums)
#
#     for i in range(len(nums)):
#         while nums[i] != '?' and nums[i] != i:
#             val = nums[i]
#             nums[i], nums[val] = nums[val], nums[i]
#         i += 1
#
#     return nums.index('?')
#
# print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
# def find_missing_numbers(nums):
#     for i in range(len(nums)):
#         while nums[i] != nums[nums[i]-1]:
#             val = nums[i]
#             nums[i], nums[val-1] = nums[val-1], nums[i]
#             print(nums)
#     missingNumbers = []
#     for i in range(len(nums)):
#         if nums[i] != i+1:
#           missingNumbers.append(i+1)
#     return missingNumbers
#
# print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
# def find_duplicate(nums):
#     i = 0
#     while i < len(nums):
#         if nums[i] != i + 1:
#             j = nums[i]-1
#             if nums[i] != nums[j]:
#                 nums[i],nums[j] = nums[j],nums[i]
#             else:
#                 return nums[i]
#         else:
#             i += 1
# print(find_duplicate([2, 1, 3, 3, 5, 4]))
# def find_all_duplicates(nums):
#     i = 0
#     while i <len(nums):
#         j = nums[i]-1
#         if nums[i] != nums[j]:
#             nums[i],nums[j] = nums[j],nums[i]
#         else:
#             i += 1
#     duplicateNumbers = []
#     for i in range(len(nums)):
#         if nums[i] != i + 1:
#             duplicateNumbers.append(nums[i])
#     return duplicateNumbers
# print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
# def find_correct_numbers(nums):
#     i = 0
#     while i < len(nums):
#         j = nums[i]-1
#         if nums[i] != nums[j]:
#             nums[i],nums[j] = nums[j],nums[i]
#         else:
#             i += 1
#     for i in range(len(nums)):
#         if nums[i] != i + 1:
#             return [nums[i], i+1]
#
# print(find_correct_numbers([3, 1, 2, 5, 2]))
# def find_subsets(nums):
#       subsets = []
#       subsets.append([])
#       for currentNumber in nums:
#         # we will take all existing subsets and insert the current number in them to create new subsets
#         n = len(subsets)
#         for i in range(n):
#               # create a new subset from the existing subset and insert the current element to it
#             set = list(subsets[i])
#             set.append(currentNumber)
#             subsets.append(set)
#
#       return subsets
# print(find_subsets([1,3]))
#
#
# def find_subsets(nums):
#     cur = [[]]
#     for val in nums:
#         nxt = []
#         for val1 in cur:
#             nxt.append(val1)
#             nxt.append([val] + val1)
#         cur = nxt
#     return cur
#
#
# print(find_subsets([1, 3]))
# def find_subsets(nums):
#     subset = [[]]
#     for val in nums:
#         nxt = []
#         for v_val in subset:
#             nxt.append(v_val)
#             set = list(subset[v_val])
#             set.append(v_val + [val])
#         set = nxt
#
#     return set
# print(find_subsets([1, 3, 3]))
# import collections
#
# def find_subsets(nums):
#   nums = collections.Counter(nums)
#
#   cur = [[]]
#   for val, frq in nums.items():
#     nxt = []
#     for count in range(frq+1):
#       nxt += [nums + [val] * count for nums in cur]
#     cur = nxt
#   return cur
# print(find_subsets([1,3,3]))

def insertion_sort(a):
    sort(0, a)

def sort(i, a):
    if i >= len(a): return False
    insert(i, a[i], a)
    sort(i + 1, a)


def insert(i, v, a):
    if i > 0 and a[i - 1] > v:
        a[i] = a[i - 1]
        insert(i - 1, v, a)
    else:
        a[i] = v

a = [4,3,2,1]
insertion_sort(a)
print(a)

