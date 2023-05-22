
def insertionSort(arr):
        size = len(arr)
        i = 1
        for i in range(size):
            j = i
            while(j > 0) and (arr[j-1]> arr[j]):
                temp = arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=temp

                j= j-1
        return arr