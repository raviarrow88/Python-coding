#bubble sort

def bubble_sort(elist):
    for i in range(1,len(elist)-1):
        for j in range(0,len(elist)-2):
            if elist[j] > elist[j+1]:
                elist[j],elist[j+1] = elist[j+1],elist[j]

    return  elist





print bubble_sort([14,46,43,27,57,41,45,21,70])




