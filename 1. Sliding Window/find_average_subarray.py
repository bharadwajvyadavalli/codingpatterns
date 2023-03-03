# finding average of subarray of size k using sliding window
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_average_subarray(arr, k):
    result = []
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:
            result.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1

    return result
