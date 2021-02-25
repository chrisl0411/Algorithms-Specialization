# Part 3 -  Assignment 1
# Problem 1: schedule jobs in decreasing order of the difference (weight-length). If tie, schedule job with higher weight first
# Report sum of weighted completion times of resulting schedule
# Problem 2: schedule jobs in decreasing order of the ratio (weight/length)

import heapq

# create an array with tuple weight/length pairs
# initiate dictionary with key = w/l pairs, value = w-l
# max heap the dictonary based on weight (invert sign on value)
# return heap
def readFile(dir, weighting):
    file = open(dir, 'r')
    numJobs = file.readline()
    jobList = []
    currLine = file.readline()

    while currLine:
        currJob = currLine.split(' ')
        currW = int(currJob[0])
        currL = int(currJob[1])
        currKey = tuple([currW, currL])
        if weighting == 'diff':
            jobList.append((currW-currL, currKey))
        elif weighting == 'ratio':
            jobList.append(((currW/currL), currKey))

        currLine = file.readline()

    heapq.heapify(jobList)
    return jobList

# largest difference in weight-len scheduled first
# if tie, higher weight job goes first
# keep on adding to length to get Cj
# calculate sum of weighted completion times for all 1>j>n, sum Wj*Cj
def calcWeightedSum(jobList):
    weightedList = heapq.nlargest(10000, jobList)
    weightedSum = 0
    aggregateTime = 0
    for i in range(len(weightedList)):
        cj = weightedList[i][1][1]
        aggregateTime += cj
        wj = weightedList[i][1][0]
        weightedSum += aggregateTime*wj

    #print(weightedList)
    print("Continual sum of time: ", aggregateTime)
    print("Sum of weighted completion times: ", weightedSum)

# schedule jobs in decreasing order of the ratio (weight/length)

if __name__ == '__main__':
    dir = 'C:\\Users\Chris\Documents\Coding\Standford Algorithms Specialization\Part 3 Greedy Algorithms and Dynamic Programming\Assignment 1\jobs.txt'

    print('Sum of weighted completion times using difference (W-L)')
    calcWeightedSum(readFile(dir, weighting='diff'))
    print('\n')
    print('Sum of weighted completion times using ratio (W/L)')
    calcWeightedSum(readFile(dir, weighting='ratio'))

