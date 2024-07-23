#Given an integer array(0-based indexing) a of size n. Your task is to return the maximum value of the sum of i*a[i] for all 0<= i <=n-1, 
#where a[i] is the element at index i in the array. The only operation allowed is to rotate(clockwise or counterclockwise) the array any number of times.

def max_sum(a,n):
    cum_sum = 0
     
    for i in range(0, n):
        cum_sum += a[i] 

    curr_val = 0
     
    for i in range(0, n):
        curr_val += i * arr[i] 
 
    # Initialize result
    res = curr_val 
 
    # Compute values for other iterations
    for i in range(1, n):

        next_val = (curr_val - (cum_sum - a[i-1]) +
                                    a[i-1] * (n-1))
 
        # Update current value
        curr_val = next_val 
 
        # Update result if required
        res = max(res, next_val)
     
    return res 