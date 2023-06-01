def pivot(arr, start, end):
    pivot = arr[start]
    swapIdx = start

    for i in range(start+1, end+1):
        if pivot > arr[i]:
            swapIdx += 1
            arr[swapIdx], arr[i] = arr[i], arr[swapIdx]

    arr[start], arr[swapIdx] = arr[swapIdx], arr[start]
    return swapIdx

def pivot(arr, pivotIndex, endIndex):
    swapIndex = pivotIndex
    for i in range(pivotIndex + 1, endIndex + 1):
        if arr[i] < arr[pivotIndex]:
            swapIndex += 1
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
    arr[pivotIndex], arr[swapIndex] = arr[swapIndex], arr[pivotIndex]
    return swapIndex


def quickSort(arr, leftPointer = 0, rightPointer = None):
    if rightPointer == None:
        rightPointer = len(arr) - 1
    if leftPointer < rightPointer:
        swapIndex = pivot(arr, leftPointer, rightPointer)
        quickSort(arr, leftPointer, swapIndex - 1)
        quickSort(arr, swapIndex + 1, rightPointer)
    return arr

print(quickSort([5,1,3,2,4])) 