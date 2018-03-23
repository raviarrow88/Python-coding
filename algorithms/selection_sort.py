#selection sort

def selection_sort(l):
    for i in range(len(l)-1):
        imin = i
        for j in range(i+1,len(l)-1):
            if l[j] < l[imin]:
                imin = j

        temp = l[i]
        l[i] = l[imin]
        l[imin]= temp

    return  l


input_list = [14, 46, 43, 27, 57 ]
print selection_sort(input_list)