#Write a Python program for sequential search.

def seq_search(l,target):
    found = False
    pos = 0

    while pos<len(l) and not found:
        if l[pos] == target:
            found = True
        else:
            pos = pos+1

    return found, pos




print(seq_search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31))
