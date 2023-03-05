'''

'''





def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()


'''
Time and Space complexity 
The above solution has the time and space complexity of O(N*S), where ‘N’ represents total numbers and ‘S’ is the required sum.

Challenge 
Can we improve our bottom-up DP solution even further? Can you find an algorithm that has O(S) space complexity?
'''