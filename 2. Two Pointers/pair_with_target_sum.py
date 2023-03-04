"""

"""


# mycode
def pair_with_target_sum(arr, target_sum):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] < target_sum:
            i += 1
        elif arr[i] + arr[j] > target_sum:
            j -= 1
        else:
            return [i, j]

    return [-1, -1]


def main():
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))


main()

'''
Time Complexity 
The time complexity of the above algorithm will be O(N), 
where ‘N’ is the total number of elements in the given array.

Space Complexity 
The space complexity will also be O(N), as, in the worst case, we will be pushing ‘N’ numbers in the HashTable.
'''
