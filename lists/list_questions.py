#1 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def count_strings(l):
    count = 0
    for i in l:
        if len(i) > 2 and i[0] == i[-1]:
            count += 1
    print count


count_strings(['abc', 'xyz', 'aba', '1221'])

#2  Remove duplicates from the list
def remove_duplicates(l):
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    print result


remove_duplicates([1, 1, 2, 3, 4, 4, 5, 7, 7])

#3 Write a Python function that takes two lists and returns True if they have at least one common member.

def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
            return result


print(common_data([1, 2, 3, 4, 5], [22, 6, 7, 8, 9]))

#4 flatten a shallow list
def flatten_list(l, flat_list):
    for i in l:
        if type(i) == list:
            flatten_list(i, flat_list)
        else:
            flat_list.append(i)

    return flat_list


flat_list = []
print flatten_list([[2, 4, 3], [1, [5, 4], 6], [9], [7, 9, 0]], flat_list)


#5 Write a python program to check whether two lists are circularly identical.

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

#6 Print the second largest element from the list

def second_largest(l):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]

    return l[-2]


print(second_largest([1, 2, -8, -2, 0]))

#7 Write a Python program to get the frequency of the elements in a list.

#Input: [10,10,10,10,20,20,20,20,40,40,50,50,30]
#output: {40: 2, 10: 4, 20: 4, 50: 2, 30: 1}

def element_frequency(l):
    count = 0
    result = {}.fromkeys(l, 0)
    for i in l:
        result[i] += 1
    print result


element_frequency([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30])


#8 Write a Python program to generate all sublists of a list.


def sub(l):
    subs = [[]]
    for i in range(len(l)):
        n = i + 1
        while n <= len(l):
            sub = l[i:n]
            subs.append(sub)
            n += 1
    print subs


sub([1, 2, 3, 4])


#9# Write a Python program to change the position of every n-th value with the (n+1)th in a list.


def replace2elements(l):
  length = len(l)
  result = []
  for i in range(length):
      while i < length:
        l[i],l[i+1] = l[i+1],l[i]
        i = i+2
      break
  print l

replace2elements([1,2,3,4,6,7])

