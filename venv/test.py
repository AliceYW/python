# def maximum69Number(num):
#     result = 0
#     swapped = False
#     v = 1000
#     while v > 0:
#         result *= 10
#         digit = num // v % 10
#         if not swapped and digit == 6:
#             result += 9
#             swapped = True
#         else:
#             result += digit
#         v //= 10
#
#     return result
#
# print(maximum69Number(9996))
# def replaceElements(arr):
#     n = len(arr)
#     result = []
#     largest = -1
#     for i in range(n - 1, -1, -1):
#         result.append(largest)
#         largest = max(largest, arr[i])
#     return result[::-1]
#
# print(replaceElements([17,18,5,4,6,1]))

# def sortString(s):
#     count = [0] * 26
#     for c in s:
#         count[ord(c) - ord('a')] += 1
#         n = len(s)
#         result = ''
#     while len(result) < n:
#         for i in range(26):
#             if count[i] > 0:
#                 count[i] -= 1
#                 result += chr(ord('a') + i)
#
#         for i in reversed(range(26)):
#             if count[i] > 0:
#                 count[i] -= 1
#                 result += chr(ord('a') + i)
#
#     return result
#
# print(sortString("aaaabbbbcccc"))
#
#
# def findMaxLength(self, nums: List[int]) -> int:
#     result = 0
#     for i in range(len(nums)):
#         count = [0, 0]
#         for j in range(i, len(nums)):
#             count[nums[j]] += 1
#             if count[0] == count[1]:
#                 result = max(result, j - i + 1)
#     return result

# def findMaxLength(nums):
#     result = 0
#     for i in range(len(nums)):
#         zero_count = 0
#         one_count = 0
#         for j in range(i, len(nums)):
#             if nums[j] == 0:
#                 zero_count += 1
#             else:
#                 one_count += 1
#
#             if zero_count == one_count:
#                 result = max(result, j - i + 1)
#     return result
#
# print(findMaxLength([0,1,1]))


# def countLetters(S):
#     n = len(S)
#     count = n
#     for i in range(n):
#         for j in range(i + 1, n):
#             if S[i] != S[j]: break
#             count += 1
#     return count
# print(countLetters('aaaba'))

list_words = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
# def uniqueMorseRepresentations(words):
#     results = set()
#
#     for word in words:
#         morse = ''.join(list_words[ord(c) - ord('a')] for c in word)
#         print(morse)
#         results.add(morse)
#
#     return len(results)
#
# print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
# def sumZero(n):
#     result = []
#     s = 0
#     for i in range(1, n):
#         result.append(i)
#         s += i
#     result.append(-s)
#     return result
#
# print(sumZero(5))
# def max_sub_arrr(k,arr):
#     max_sum = 0
#     for i in range(len(arr)-k+1):
#         sum_num = 0
#         for j in range(i, i+k):
#             sum_num += arr[j]
#             max_sum = max(sum_num, max_sum)
#     return max_sum
#
#
# print(max_sub_arrr(3,[2,1,5,1,3,2]))

# def max_sub_array_of_size_k(k, arr):
#     i = 1
#     j = i+k-1
#     sum_arr = sum(arr[:k])
#     print(sum_arr)
#     min_sum = sum_arr
#     while j < len(arr):
#         sum_arr += arr[j] - arr[i-1]
#         min_sum = min(min_sum, sum_arr)
#         i += 1
#         j += 1
#     return min_sum
#
# print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))

# def smallest_subarray_with_given_sum(s, arr):
#     i = 0
#     smallest_subarr = float('inf')
#     sum_arr = 0
#     for j in range(len(arr)):
#         sum_arr += arr[j]
#         while sum_arr - arr[i] >= s:
#             sum_arr -= arr[i]
#             i += 1
#             if sum_arr >= s:
#                 smallest_subarr = min(smallest_subarr, j-i+1)
#     return smallest_subarr
#     # for i in range(len(arr)):
#     #   sum_arr += arr[i]
#     #   while sum_arr >= s:
#     #     min_length = min(min_length, i-start+1)
#     #     sum_arr -= arr[start]
#     #     start += 1
#
#     return smallest_subarr
# print(smallest_subarray_with_given_sum(7,[2, 1, 5, 2, 8]))
# import collections
# def longest_substring(str, k):
#     n = len(str)
#     longest = -1
#     i = 0
#     counter = collections.Counter()
#     unique_chars = 0
#     for j in range(n):
#         newest_char = str[j]
#         if counter[newest_char] == 0: unique_chars += 1
#         counter[newest_char] += 1
#         while unique_chars > k:
#             oldest_char = str[i]
#             counter[oldest_char] -= 1
#             if counter[oldest_char] == 0: unique_chars -= 1
#             i += 1
#         longest = max(longest, j - i + 1)
#     return longest
# print(longest_substring("araaci", 2))

# def fruits_into_baskets(fruits):
#     start_window = 0
#     most_fruits = 0
#     f1, c1 = None, 0
#     f2, c2 = None, 0
#
#     for end_window in range(len(fruits)):
#         cur_fruit = fruits[end_window]
#
#         while f1 != cur_fruit and f2 != cur_fruit and c1 > 0 and c2 > 0:
#             last_fruit = fruits[start_window]
#             if f1 == last_fruit:
#                 c1 -= 1
#             elif f2 == last_fruit:
#                 c2 -= 1
#             start_window += 1
#
#         if cur_fruit == f1:
#             c1 += 1
#         elif cur_fruit == f2:
#             c2 += 1
#         elif c1 == 0:
#             f1, c1 = cur_fruit, 1
#         elif c2 == 0:
#             f2, c2 = cur_fruit, 1
#
#         most_fruits = max(most_fruits, c1 + c2)
#     return most_fruits
# print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))

# def non_repeat_substring(str):
#     start_window = 0
#     char_map = {}
#     max_length = 0
#     for end_window in range(len(str)):
#         right_char = str[end_window]
#         if right_char in char_map:
#             start_window = max(start_window, char_map[right_char]+1)
#         char_map[right_char] = end_window
#         print(char_map)
#         max_length = max(max_length,end_window - start_window + 1)
#     return max_length
# print(non_repeat_substring("aabccbb"))

# import collections
#
# def length_of_longest_substring(str, k):
#     str_len = len(str)
#     start_idx = 0
#     end_idx = 0 # not part of window (exclusive)
#
#     longest_substr = 0
#
#     char_count = collections.Counter()
#     freq_chars = collections.defaultdict(set)
#
#     highest_freq = 0
#
#     while end_idx < str_len:
#
#         while end_idx < str_len and (str[end_idx] in freq_chars[highest_freq] or end_idx - start_idx - highest_freq < k):
#             freq_chars[char_count[str[end_idx]]] -= {str[end_idx]}
#             char_count[str[end_idx]] += 1
#             freq_chars[char_count[str[end_idx]]] |= {str[end_idx]}
#
#             if char_count[str[end_idx]] > highest_freq:
#                 highest_freq += 1
#
#             end_idx += 1
#
#         longest_substr = max(longest_substr, end_idx - start_idx)
#
#         if highest_freq == char_count[str[start_idx]] and len(freq_chars[char_count[str[start_idx]]]) == 1:
#             highest_freq -= 1
#         freq_chars[char_count[str[start_idx]]] -= {str[start_idx]}
#         char_count[str[start_idx]] -= 1
#         freq_chars[char_count[str[start_idx]]] |= {str[start_idx]}
#
#         start_idx += 1
#
#     return longest_substr
#
# print(length_of_longest_substring("aabccbb", 2))

# def pair_with_targetsum(arr, target_sum):
#     start_point = 0
#     end_point = len(arr)-1
#     while(start_point < end_point):
#         current_sum = arr[start_point] + arr[end_point]
#         if current_sum == target_sum:
#             return [start_point, end_point]
#         elif arr[start_point] + arr[end_point] < target_sum:
#             start_point += 1
#         else:
#             end_point -= 1
#
# print(pair_with_targetsum([2,5,9,11], 11))

# def remove_duplicates(arr):
#     next = 1
#     i = 1
#     while i < len(arr):
#         if arr[next-1] != arr[i]:
#             arr[next] = arr[i]
#             next += 1
#         i += 1
#     return next
#
#
# print(remove_duplicates([2,3,3,3,6,9,9]))
# def remove_element(arr, key):
#     i, j = 0, 0
#     while i < len(arr):
#         if arr[i] != key:
#             arr[i],arr[j] = arr[j],arr[i]
#             j += 1
#         i += 1
#     return j
#
#
# print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
# print(remove_element([2, 11, 2, 2, 1], 2))

# def make_squares(arr):
#     new_squares = []
#     for i in range(len(arr)):
#         new_arr = abs(arr[i] * 2)
#         new_squares.append(new_arr)
#         squares = new_squares
#         j,k = 0,0
#         while j < len(squares):
#             if j < k:
#                 squares[j],squares[k] = squares[k],squares[j]
#                 k += 1
#             j += 1
#     return squares
#
# print(make_squares([-2, -1, 0, 2, 3]))
# def search_triplets(arr):
#     arr.sort()
#     triplets = []
#     for i in range(len(arr)):
#         if i > 0 and arr[i] == arr[i-1]:
#             continue
#         search_pair(arr, -arr[i], i+1, triplets)
#     return triplets
#
# def search_pair(arr, target_sum, left, triplets):
#     right = len(arr)-1
#     while(left < right):
#         current_sum = arr[left] + arr[right]
#         if current_sum == target_sum:
#             triplets.append([-target_sum, arr[left], arr[right]])
#             left += 1
#             right -= 1
#             while left < right and arr[left] == arr[left-1]:
#                 left += 1
#             while left < right and arr[right] == arr[right+1]:
#                 right -= 1
#         elif target_sum > current_sum:
#             left += 1
#         else:
#             right -= 1
# print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))

# def make_squares(arr):
#   n = len(arr)
#   squares = [0 for x in range(n)]
#   highestSquareIdx = n - 1
#   left, right = 0, n - 1
#   while left <= right:
#     leftSquare = arr[left] * arr[left]
#     rightSquare = arr[right] * arr[right]
#     if leftSquare > rightSquare:
#       squares[highestSquareIdx] = leftSquare
#       left += 1
#     else:
#       squares[highestSquareIdx] = rightSquare
#       right -= 1
#     highestSquareIdx -= 1
#
#   return squares
# print(make_squares([-2, -1, 0, 2, 3]))
# def find_happy_number(num):
#     slow,fast = num,num
#     while True:
#         slow = find_squares_sum(slow)
#         fast = find_squares_sum(find_squares_sum(fast))
#         if slow == fast:
#             break
#     return slow == 1
#
# def find_squares_sum(num):
#
#     sum_digit = 0
#     while num > 0:
#         digit = num % 10
#         sum_digit += digit * digit
#         num = num // 10
#     return sum_digit
#     print(sum_digit)
#
#
# print(find_happy_number(23))

# def isPalindrome(x):
#     if x < 0: return False
#     digit = 0
#     cur = x
#     while cur:
#         digit *= 10
#         digit += cur % 10
#         cur //= 10
#     return x == digit
# print(isPalindrome(121))

# class interval:
#   def __init__(self, start, end):
#     self.start = start
#     self.end = end
#
#     def merge(intervals):
#         if len(intervals) < 2:
#             return intervals
#
#         # sort the intervals on the start time
#         intervals.sort(key=lambda x: x.start)
#         mergedIntervals = []
#         start = intervals[0].start
#         end = intervals[0].end
#         for i in range(1, len(intervals)):
#             interval = intervals[i]
#             if interval.start <= end:  # overlapping intervals, adjust the 'end'
#               end = max(interval.end, end)
#             else:  # non-overlapping interval, add the previous internval and reset
#               mergedIntervals.append(Interval(start, end))
#               start = interval.start
#               end = interval.end
#
#         # add the last interval
#         mergedIntervals.append(Interval(start, end))
#         return mergedIntervals
# print(interval([[1,4], [2,5], [7,9]]))
# def merge_ranges(meetings):
#     sorted_meetings = sorted(meetings)
#     merged_meetings = [sorted_meetings[0]]
#     for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
#         last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
#         print(merged_meetings[-1])
#         if (current_meeting_start <= last_merged_meeting_end):
#             merged_meetings[-1] = (last_merged_meeting_start,max(last_merged_meeting_end,current_meeting_end))
#         else:
#             merged_meetings.append((current_meeting_start, current_meeting_end))
#     return merged_meetings
# print(merge_ranges([[1,4], [2,5], [7,9]]))

# print(reverse(list_of_char))
# message = ['c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]
# def reverse_words(message):
#     reverse_characters(message, 0, len(message) - 1)
#     current_word_start_index = 0
#     for i in range(len(message) + 1):
#         if (i == len(message)) or (message[i] == ' '):
#             reverse_characters(message, current_word_start_index, i - 1)
#             current_word_start_index = i + 1
#
#
# def reverse_characters(message, left_index, right_index):
#     while left_index < right_index:
#         # Swap the left char and right char
#         message[left_index], message[right_index] = message[right_index], message[left_index]
#         left_index += 1
#         right_index -= 1
#
# reverse_words(message)
# print(''.join(message))
# def insert(intervals,new_interval):
#         merged = []
#         i, start, end = 0, 0, 1
#
#         # skip (and add to output) all intervals that come before the 'new_interval'
#         while i < len(intervals) and intervals[i][end] < new_interval[start]:
#             merged.append(intervals[i])
#             i += 1
#
#         # merge all intervals that overlap with 'new_interval'
#         while i < len(intervals) and intervals[i][start] <= new_interval[end]:
#             new_interval[start] = min(intervals[i][start], new_interval[start])
#             new_interval[end] = max(intervals[i][end], new_interval[end])
#             i += 1
#
#         # insert the new_interval
#         merged.append(new_interval)
#
#         # add all the remaining intervals to the output
#         while i < len(intervals):
#             merged.append(intervals[i])
#             i += 1
#         return merged
#
# print(insert([[1,3], [5,7], [8,12]],[4,6]))
# def can_attend_all_appointments(intervals):
#   intervals.sort(key=lambda x:x[0])
#   start, end = 0, 1
#   result = []
#   for i in range(1, len(intervals)):
#     if intervals[i][start] < intervals[i-1][end]:
#         return True
#   return False
# print(can_attend_all_appointments([[4,5], [2,3], [3,6]]))
# def find_missing_number(nums):
#   i = 0
#   while i < len(nums):
#     j = nums[i]
#     if nums[i] < len(nums) and nums[i] != nums[j]:
#         nums[i],nums[j] = nums[j],nums[i]
#     else:
#         i += 1
#   for i in range(len(nums)):
#       if nums[i] != i:
#           return i
#   return i
# print(find_missing_number([4,0,3,1]))
# def cyclic_sort(nums):
#   i = 0
#   while i < len(nums):
#     j = nums[i] - 1
#     if nums[i] != nums[j]:
#       nums[i], nums[j] = nums[j], nums[i]  # swap
#     else:
#       i += 1
#   return nums
# print(cyclic_sort([3, 1, 5, 4, 2]))

# def find_subsets(nums):
#   list.sort(nums)
#   subsets = []
#   subsets.append([])
#   startIndex, endIndex = 0, 0
#   for i in range(len(nums)):
#     startIndex = 0
#     if i > 0 and nums[i] == nums[i - 1]:
#       startIndex = endIndex + 1
#     endIndex = len(subsets) - 1
#     for j in range(startIndex, endIndex+1):
#       set = list(subsets[j])
#       set.append(nums[i])
#       subsets.append(set)
#   return subsets
# print(find_subsets([1,3,3]))
# def find_max_in_bitonic_array(arr):
#   start, end = 0, len(arr) - 1
#   while start < end:
#     mid = start + (end - start) // 2
#     if arr[mid] > arr[mid + 1]:
#       end = mid
#     else:
#       start = mid + 1
#   return arr[end]
# print(find_max_in_bitonic_array([10,9,8]))
# def find_missing_number(arr):
#     n = len(arr)+1
#     s1 = 0
#     for i in range(0, n+1):
#         s1 += i
#     for i in arr:
#         s1 -= i
#     return s1
#
# print(find_missing_number([1,5,2,6,4]))
# from heapq import *
#
# def find_k_largest_numbers(nums, k):
#   minHeap = []
#   for i in range(k):
#     heappush(minHeap, nums[i])
#   for j in range(k, len(nums)):
#     if nums[j] > minHeap[0]:
#       heappop(minHeap)
#       heappush(minHeap, nums[j])
#   return list(minHeap)
# print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))
# from heapq import *
# def find_smallest_number(nums,k):
#   maxHeap = []
#   for i in range(k):
#     heappush(maxHeap, -nums[i])
#     for j in range(k,len(nums)):
#       if nums[j] > maxHeap[0]:
#         heappop(maxHeap)
#         heappush(maxHeap, -nums[j])
#   return -maxHeap[0]
#
# print(find_smallest_number([1, 5, 12, 2, 11, 5], 3))
# from heapq import *
# def find_smallest_number(nums,k):
#   minHeap = []
#   for i in range(len(nums)):
#       heappush(minHeap, -nums[i])
#       if -nums[i] > minHeap[0]:
#           heappop(minHeap)
#           print(minHeap)
#   return -minHeap[0]
#
# print(find_smallest_number([5, 12, 11, -1, 12], 3))
# from heapq import *
# def minimum_cost_to_connect_ropes(ropeLegths):
#     minHeap = []
#     for i in range(len(ropeLegths)):
#         heappush(minHeap, ropeLegths[i])
#     result,temp = 0,0
#     while len(minHeap) > 1:
#         temp = heappop(minHeap) + heappop(minHeap)
#         result += temp
#         heappush(minHeap, temp)
#     return result
#
# print(minimum_cost_to_connect_ropes([1, 3, 11, 5]))
# def isVowel(character):
#   character = character.lower()
#
#   vowels = "aeiou"
#   if character in vowels :
#     return 1
#   else:
#       return 0
#
# def countVowels(string, n): # function that returns the count of vowels
# 	# Base Case
#   if n == 1 :
# 	  return isVowel(string[0])
#
#   return countVowels(string, n - 1) + isVowel(string[n - 1])
# string = "Educative"
# print(countVowels(string, len(string)))
# def findSquare(targetNumber) :
#   if targetNumber == 0: return 0
#   return findSquare(targetNumber - 1) + (2 * targetNumber) - 1
# print(findSquare(5))

# result = [1]
# target_row = 5
# for _ in range(target_row):
#     next_row = []
#     for i in range(len(result)-1):
#         next_row.append(result[i] + result[i+1])
#     result = [1] + next_row + [1]
#
# print(result)
# def remove(string):
#   if not string:
#       return ""
#   if string[0] == "\t" or string[0] == " ":
#       return remove(string[1:])
#   else:
#       return string[0] + remove(string[1:])
#
# print(remove("Hello Wo\trld"))
# def isPalidrome(testVariable):
#     if len(testVariable) <= 1:
#         return True
#     if testVariable[0] == testVariable[len(testVariable)-1]:
#         return isPalidrome(testVariable[1:len(testVariable)-1])
#     return False
# print(isPalidrome("mdiadm"))

# def count(array, key) :
#   if array == []:
#       return 0
#   if array[0] == key:
#       return 1 + count(array[1:], key)
#   else:
#       return 0 + count(array[1:], key)
# array = [1, 2, 1, 4, 5, 1]
# key  = 1
# print(count(array, key))
# def average(testVariable, currentIndex=0):
#     if currentIndex == len(testVariable) - 1:
#         return testVariable[currentIndex]
#     print(testVariable[currentIndex])
#
#     if currentIndex == 0:
#         return ((testVariable[currentIndex]+average(testVariable, currentIndex + 1))/len(testVariable))
#
#     return (testVariable[currentIndex]+average(testVariable, currentIndex + 1))
# print(average([10, 2, 3, 4, 8, 0],0))
# def balanced(testVariable, startIndex = 0, currentIndex = 0):
#     if startIndex == len(testVariable): return currentIndex
#     if currentIndex < 0: return False
#     if testVariable[startIndex] == "(":
#         return balanced(testVariable,startIndex+1,currentIndex+1)
#     elif testVariable[startIndex] == ")":
#         return balanced(testVariable,startIndex+1,currentIndex-1)
#
# print(balanced(["(", ")", "(", ")", "("]))

# def sortArr(testVariable, length):
#     if length <= 1:
#         return False
#     sortArr(testVariable, length-1)
#
#     lastElement = testVariable[length-1]
#     temp = length-2
#     while (temp >= 0 and testVariable[temp] > lastElement):
#         testVariable[temp+1] = testVariable[temp]
#         temp = temp - 1
#     testVariable[temp+1] = lastElement
# testVariable = [5,4,2,3,1]
# sortArr(testVariable,5)
# print(testVariable)

# my_list = [5,2,3,4,1]
# def bubble(bad_list):
#     length = len(bad_list) - 1
#     sorted = False
#     while not sorted:
#         sorted = True
#         for i in range(length):
#             if bad_list[i] > bad_list[i+1]:
#                 sorted = False
#                 bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
#
# bubble(my_list)
# print (my_list)