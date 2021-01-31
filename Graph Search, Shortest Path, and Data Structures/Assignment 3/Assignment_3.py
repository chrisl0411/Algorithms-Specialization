# Assignment 3 - Median Maintenance
# compute sum of 10000 medians using heaps

import heapq

def readFile(dir):
    numbers = []
    file = open(dir, 'r')
    current_line = file.readline()
    while current_line:
        numbers.append(int(current_line))
        current_line = file.readline()
    return numbers

# if k is odd, then mk is ((k+1)/2)th smallest number, if k is even, then mk is (k/2th smallest number)
def median(numbers):
    sample = [numbers[0]]
    heapq.heapify(sample)
    sum = sample[0]
    # insert ith integer from numbers into sample
    for i in range(1, 10000):
        k = i+1
        heapq.heappush(sample, numbers[i])
        if k%2 == 1:
            medIndex = int((k+1)/2)
        elif k%2 == 0:
            medIndex = int((k/2))
        sum += heapq.nsmallest(medIndex, sample)[-1]
    print(len(sample))

    return sum

if __name__ == "__main__":
    dir = "C:\\Users\Chris\Documents\Coding\Standford Algorithms Specialization\Part 2_Graphs\Assignment3_Median.txt"
    sum = 0
    print(median(readFile(dir)))