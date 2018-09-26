def bubble_sort(alist):
    for i in range(len(alist)):
        for j in range(len(alist)-1):
            if alist[j] > alist[i]:
                alist[j],alist[i]=alist[i],alist[j]



def insertion_sort(alist):
    for i in range(1, len(alist)):
        current_value = alist[i]
        position      = i
        while position > 0 and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            position -= 1
            alist[position] = current_value


# The next 3 algorithms are examples of "Prefix Average" algorithms, and each function
# is a different timing-type of algorithm.
#
# If you don't know what a 'Prefix Average' is, it's worthwhile to readup on, because it
# has a multitude of applicable scenarios.  Of which are not limited to any one domain.
# 
# Also, these prefix algorithms are not my code; they are courtesy of a super-expensive
# textbook ;)
#


# A Quadratic-Time Algorithm: O(n^2)
def prefix_average1(S):
    """ Return list such that, for all j, A[j] equals average of S[0], ..., S[j]. """
    n = len(S)                      # executed in Constant-Time O(1)
    A = [0] * n                     # create new list of n zeros, and uses a constant
                                    # number of primitive operations per element, so it
                                    # runs in Linear-Time --> O(n)
    for j in range(n):
        total = 0                   # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j+1)        # record the average
    return A







if __name__ == '__main__':
    # Add testing code, once not using 'Sorting_and_Timing_Lab.py' as the testing source.
