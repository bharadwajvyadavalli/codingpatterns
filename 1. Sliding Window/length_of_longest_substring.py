"""
Problem Statement
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""


# mycode
def length_of_longest_substring(arr, k):
    win_start, max_len, cnt = 0, 0, 0
    zero_position = [0] * (k + 1)

    for win_end in range(len(arr)):
        if arr[win_end] == 0:
            cnt += 1
            zero_position[cnt - 1] = win_end

            if cnt > k:
                win_start = zero_position[0] + 1
                zero_position = zero_position[1:] + [0]
                cnt -= 1

        max_len = max(max_len, win_end - win_start + 1)

    return max_len


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()

'''
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the count of numbers in the input array.

Space Complexity 
The algorithm runs in constant space O(1).
'''
