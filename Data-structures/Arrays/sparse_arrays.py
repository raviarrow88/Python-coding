'''
There is a collection of N strings ( There can be multiple occurences of a particular string ).
 Each string's length is no more than 20 characters. There are also Q queries.
For each query, you are given a string, and you need to find out how many times this string occurs in the given collection of N strings.

Input Format

The first line contains N , the number of strings.
The next N lines each contain a string.
The N+2nd line contains ,Q the number of queries.
The following Q lines each contain a query string.

Sample Input

4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Sample Output

2
1
0

'''

#solution


def stringOccur(strings,qs_list):
    for query in qs_list:
        count = 0
        for string in strings:
            if query == string:
                count =count +1
        yield  count


if __name__ == '__main__':
    n = int(raw_input())
    strings = []
    for i in range(n):
        string =  raw_input()
        strings.append(string)
    nq = int(raw_input())
    qs_list = []
    for i in range(nq):
        queries = raw_input()
        qs_list.append(queries)

    result = stringOccur(strings,qs_list)
    for i in result:
        print i
