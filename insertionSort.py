def insertionSort(array):
    i = 0
    j = 1
    k = 1
    size = len(array)

    if(size>1):
        UnSorted = True

        while(k!=size):
            while(UnSorted):
                if(array[j] < array[i]): # If j is smaller than i
                    new = array[j]
                    k=j
                    for i in range(k):
                        if (k!=size):
                            array[k+1] = array[k]
                            k+=1

                j+=1 
            



array = [30,10,4,5,18,8]
insertionSort(array)
print(array)