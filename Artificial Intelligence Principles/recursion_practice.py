import random


# computes the nth fibonacci number
#n is the number index and needs to be greater than 1 at least
def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

#computes the n factorial (n!)
#this uses a brute force linear complexity algorithm
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

print(fact(4))


def binary_search(arr, startPos, endPos, searchNum):
    arr=[]
    if endPos >= startPos:
        mid = startPos + (endPos - startPos)/2
        if arr[mid] > searchNum:
            return mid
        if arr[mid] == searchNum:
            return binary_search(arr, startPos, mid-1, searchNum)
        return binary_search(arr, mid+1, endPos, searchNum)
    return -1

print(binary_search(100, 10, 110, 5))
                                 
