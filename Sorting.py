def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort([5,1,3,2,4]))

def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

print(selection_sort([5,1,3,2,4]))


def insertion_sort(array):
    for i in range(1, len(array)):
        # for j in range(i, 0, -1):
        #     if array[j-1] > array[j]:
        #         array[j-1], array[j] = array[j], array[j-1]
        #     else:
        #         break
        temp = array[i]
        j = i-1
        while j >= 0 and temp < array[j] :
                array[j + 1] = array[j]
                array[j] = temp
                j -= 1
    return array

print(insertion_sort([5,1,3,2,4]))