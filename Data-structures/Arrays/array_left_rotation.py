
'''
A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array , then the array would become .

Given an array of n integers and a number, d, perform  left rotations on the array. Then print the updated array as a single line of space-separated integers.

Input Format

The first line contains two space-separated integers denoting the respective values of n (the number of integers) and d (the number of left rotations you must perform).
The second line contains n space-separated integers describing the respective elements of the array's initial state.



Output Format

Print a single line of n space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4


'''






#solution

def leftRotation(a,d,n):
    for i in range(d):
        temp = a[0]
        for i in range(0, n - 1):
            a[i] = a[i + 1]
        a[n - 1] = temp
    return a




if __name__ == "__main__":
    n, d = raw_input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = map(int, raw_input().strip().split(' '))
    result = leftRotation(a, d, n)
    print " ".join(map(str, result))
