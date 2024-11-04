#Write a function longest_subarray(array) that takes a binary list 
#(containing only 0s and 1s) as input and returns the length of the longest 
#adjacent subarray with an equal number of 0s and 1s.

def longest_subarray(array):
    max_length = 0

    #  starting points of the subarray
    for start in range(len(array)):
        #  ending points of the subarray
        for end in range(start + 1,len(array) + 1):
            subarray = array[start:end]
            # Count the number of 0s and 1s
            count_0 = subarray.count(0)
            count_1 = subarray.count(1)
            # If they are equal, check the length
            if count_0 == count_1:
                max_length = max(max_length, end - start)

    return max_length

# Example usage:
binary_array = [0, 0, 1, 1, 1, 1]
print(longest_subarray(binary_array)) 

     

#example
#[0, 0, 1, 1, 1, 1]
#take the minimum count which is 0,0
# [0,0,1,1]