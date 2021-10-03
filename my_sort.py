def sort(list):
    if len(list) > 1:
 
        # Finding the mid of the array
        mid = len(list)//2
 
        # Dividing the array elements
        L = list[:mid]
 
        # into 2 halves
        R = list[mid:]
 
        # Sorting the first half
        sort(L)
 
        # Sorting the second half
        sort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1 
    return list

if __name__ == "__main__":
    result = sort(["hello", "abc", "obb", "bob","dab","monster"])
    print(result)