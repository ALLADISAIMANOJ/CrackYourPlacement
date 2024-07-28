# Python3 program to Rearrange
# an array so that arr[i] becomes
# arr[arr[i]]

# The function to rearrange an
# array in-place so that arr[i]
# becomes arr[arr[i]].


def rearrange(arr, n):

	# First step: Increase all values
	# by (arr[arr[i]] % n) * n
	for i in range(0, n):
		arr[i] += (arr[arr[i]] % n) * n

	# Second Step: Divide all values
	# by n
	for i in range(0, n):
		arr[i] = int(arr[i] / n)

# A utility function to print
# an array of size n

def printArr(arr, n):

	for i in range(0, n):
		print(arr[i], end=" ")
	print("")


# Driver program
arr = [3, 2, 0, 1]
n = len(arr)

print("Given array is")
printArr(arr, n)

rearrange(arr, n)
print("Modified array is")
printArr(arr, n)

