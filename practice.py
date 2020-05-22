# def isVowel(character):
#     character = character.lower()
#     vowel = 'aeiou'
#     if character in vowel:
#         return 1
#     else:
#         return 0
#
#
# def countVowels(string, n):
#     if n == 1:
#         return isVowel(string[0])
#     return countVowels(string, n - 1) + isVowel(string[n - 1])
#
#
#
# string = 'educative'
# print(countVowels(string, len(string)))
# def printPascal(testVariables):
#     if testVariables == 0:
#         return [1]
#     else:
#         line = [1]
#
#         previousLine = printPascal(testVariable - 1)
#         for i in range(len(previousLine) - 1):
#             line.append(previousLine[i] + previousLine[i + 1])
#         line += [1]
#     return line
#
#
# print(printPascal(5))
# def count(array, key):
#     if not array:
#         return 0
#     if array[0] == key:
#         return 1 + count(array[1:], key)
#     else:
#         return 0 + count(array[1:], key)
#
# print(count([1, 2, 1, 4, 5, 1], 1))

# def average(testVariable, currentIndex = 0):
#     if currentIndex == len(testVariable)-1:
#         return testVariable[currentIndex]
#     if currentIndex == 0:
#         return (testVariable[currentIndex] + average(testVariable, currentIndex+1)) / len(testVariable)
#     return testVariable[currentIndex] + average(testVariable, currentIndex+1)
# print(average([10,2,3,4,8,0]))
# def max_sub_array_of_size_k(k, arr):
#     max_sum = 0
#     window_sum = 0
#     for i in range(len(arr)-k+1):
#         window_sum = 0
#         for j in range(i, i+k):
#             window_sum += arr[j]
#         max_sum = max(max_sum, window_sum)
#     return max_sum
# print(max_sub_array_of_size_k(3, [2,1,5,1,3,2]))
# def max_sub_array_of_size_k(k, arr):
#     max_sum = 0
#     window_sum = 0
#     window_start = 0
#     for i in range(len(arr)):
#         window_sum += arr[i]
#         if i >= k-1:
#             max_sum = max(max_sum, window_sum)
#             window_sum -= arr[window_start]
#             window_start += 1
#     return max_sum
#
# print(max_sub_array_of_size_k(3, [2,1,5,1,3,2]))
# def smallest_subarray_with_given_sum(s, arr):
#     i = 0
#     sum_arr = 0
#     min_length = float('inf')
#     for j in range(len(arr)):
#         sum_arr += arr[j]
#         while sum_arr - arr[i] >= s:
#             sum_arr -= arr[i]
#             i += 1
#             if sum_arr >= s:
#                 min_length = min(min_length, j-i+1)
#     return min_length
#
# print(smallest_subarray_with_given_sum(8,[3,4,1,1,6]))
# def smallest(s, arr):
#     window_sum = 0
#     min_length = float('inf')
#     window_start = 0
#     for i in range(len(arr)):
#         window_sum += arr[i]
#         while window_sum >= s:
#             min_length = min(min_length, i - window_start+1)
#             window_sum -= arr[window_start]
#             window_start += 1
#     return min_length
# print(smallest(8, [3,4,1,1,6]))
# def longest_substring_with_k_distinct(str, k):
#     window_start = 0
#     char_frequency = {}
#     longest_length = 0
#     for i in range(len(str)):
#         right_char = str[i]
#         if right_char not in char_frequency:
#             char_frequency[right_char] = 0
#         char_frequency[right_char] += 1
#         while len(char_frequency) > k:
#             left_char = str[window_start]
#             char_frequency[left_char] -= 1
#             if char_frequency[left_char] == 0:
#                 del char_frequency[left_char]
#             window_start += 1
#         longest_length = max(longest_length, i-window_start+1)
#     return longest_length
#
#
# print(longest_substring_with_k_distinct('araaci', 2))
# def pair_with_targetsum(arr, target_sum):
#     window_start = 0
#     window_end = len(arr) - 1
#     while window_start < window_end:
#         current_sum = arr[window_start] + arr[window_end]
#         if current_sum == target_sum:
#             return [window_start, window_end]
#         if target_sum > current_sum:
#             window_start += 1
#         else:
#             window_end -= 1
#
#
# print(pair_with_targetsum([2, 5, 9, 11], 11))
# def remove_duplicates(arr):
#     next_non_duplicate = 1
#     i = 1
#     while i < len(arr):
#         if arr[next_non_duplicate-1] != arr[i]:
#             arr[next_non_duplicate] = arr[i]
#             next_non_duplicate += 1
#             print(next_non_duplicate)
#         i += 1
#     return next_non_duplicate
# print(remove_duplicates([2,3,3,3,6,9,9]))
def remove_element(arr, key):
    next_element = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_element] = arr[i]
            next_element += 1
    return next_element
print(remove_element([3,2,3,6,3,10,9,3], 3))