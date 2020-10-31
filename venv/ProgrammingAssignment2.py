#Stanford Algorithms Specialization Part 1 Divide and Conquer
#Programming Assignment #2

#Goal: compute number of inversions in the file given where the ith row of the file indicates the ith entry of an array
#An inverstion = a pair of array indices with i<j and A[i]>A[j]
#if x copied to merge array before y, then x<y and no inversion involving x and y
#if y copied to merge array before x, then x>y and split inversion is present
#when element of 2nd array C gets copied to output D, increment total by number of elements remaining in 1st array B

import os

def readFile():
    filePath = "C:\\Users\Chris\Documents\Coding\Standford Algorithms Specialization\Part 1_Divide and Conquer\IntegerArray.txt"
    f = open(filePath, "r")
    array = []
    while (f.readline()) :
        array.append(int(f.readline()))

    length = len(array)
    return array

def countSplitInv(x, y):
    i = 0
    j = 0
    count = 0
    result = []

    while (i < len(x) and j < len(y)):
        if (x[i] < y[j]):
            result.append(x[i])
            i+=1
        else:
            count+= len(x)-i #adds number of remaining elements in x to split inv count
            result.append(y[j])
            j+=1

    result+=left[i:]
    result+=right[j:]

    return result, count

def sort(array):
    #high level aglorithm
    #base case
    n = len(array)
    if (n == 1):
        return 0
    else:
        middleIndex = int(n/2)
        x = sort(array[:middleIndex])[0]
        y = sort(array[middleIndex:])[0]
        sortedlist, count = countSplitInv(x, y)

    return sortedlist, count

if __name__ == "__main__":
    print(sort(readFile())[1])