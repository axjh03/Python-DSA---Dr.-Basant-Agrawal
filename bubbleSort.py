# # Swapping in Python
# int1 = 10;int2 = 20

# # Printing the values
# print(int1,int2)

# # Swapping
# int1,int2 = int2, int1

# # Printing the values
# print(int1,int2)

import random as rand

# Coding Bubble Sort Algorithm
def bubbleSort(array):
    Unsorted = True; size = len(array); i=j=k=0
    while Unsorted:
        k+=1
        for i in range(size):
            if(i != size-1):
                j=i+1
            if(array[i] > array[j]):
                array[i], array[j] = array[j],array[i]
                print(f"[Unsorted] Swapping {array[j]} with {array[i]}   -->   ", end = "")
                print(array)
                i+=1
            else:
                i+=1
            if(k==size):
                Unsorted = False

if __name__ =="__main__":
    #arr = [100,20,30,40,2,30,21,4,91,104]
    arr = []
    for i in range(10):
        newElement = rand.randint(29,80)
        newList = [newElement]
        arr.append(newList)

    print("Unsorted Array ", end="")
    print(arr,end="\n\n\n")
    bubbleSort(arr)
    print("\n\n\n")
    print("[Sorted]  Sorted Array  --->   ", end="")
    print(arr,end="\n")