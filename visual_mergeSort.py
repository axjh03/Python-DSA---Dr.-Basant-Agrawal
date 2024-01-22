# Defining the MergeSort function
def mergeSort(array):
    if(len(array))>1: # Only keep on dividing until the array has size no more than 1

        # Find the middle of the array
        mid = len(array)//2 

        # Slicing / splitting
        left = array[:mid]
        right = array[mid:]
        print(f"Splitted left : {left}")
        print(f"Splitted right : {right}")


        # Creating reccursion enviroments
        mergeSort(left)
        mergeSort(right)

        # Create/reset the counters
        i=j=k=0

        # Compare and copy
        while(i<len(left) and j<len(right)):
            if(left[i]<right[j]):
                array[k] = left[i]
                print(f"copying {left[i]} to {k}th inde of array")
                i+=1
            
            else:
                array[k] = right[j]
                print(f"copying {right[j]} to {k}th inde of array")
                j+=1
            
            k+=1

        # Copy the rest 
        while(i<len(left)):
            array[k] = left[i]
            i+=1
            k+=1

        while(j<len(right)):
            array[k] = right[j]
            j+=1
            k+=1


# Driver Code
if __name__ == "__main__":
    array = [30,50,50,10,70,33,99,33,28,98,1000,1,4,6,3,2,21,53]
    print("Unsorted array : ", end="")
    print(array)
    mergeSort(array)
    print("Sorted array : ", end="")
    print(array)