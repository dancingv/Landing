"""
这里也可以写
"""
def multiply(a,b):
    """
    >>> multiply(2,3)
    6
    >>> multiply('baka~',3)
    'baka~baka~baka~'
    """
    return a*b

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)
#quick sort快排
def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i+1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L
LL01 = [22,33,11,23.2,45.2,12.4,563.1,1245.4,12.45]
ll02 = quickSort(LL01,0,len(LL01)-1)
print(ll02)