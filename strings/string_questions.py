'''this file contains the commonly asked list programming questions'''

#1 Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def character_frequency(string):
    result = {}
    for i in string:
        keys = result.keys()

        if i in keys:
            result[i] += 1
        else:
            result[i] = 1
    print result


character_frequency('goodmorning')


#2 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

def string_ends(string):
    length = len(string)
    if length < 2:
        return " "

    return string[0:2]+string[-2:]

print string_ends('helloworld')
print string_ends('w')

#3 Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
def swap_first_two(string1,string2):
    new_string1 = string2[:2]+string1[2:]
    new_string2 = string1[:2]+string2[2:]

    return  '{} {}'.format(new_string1,new_string2)

print(swap_first_two('abc', 'xyz'))


#4 Write a Python function that takes a list of words and returns the length of the longest one.

def longest_length(l):
    result = []
    for i in l:
        result.append((len(i), i))
    result.sort()
    print result[-1][0]


longest_length(['good', 'morning', 'world'])


#5 Write a Python program to change a given string to a new string where the first and last chars have been exchanged.


def string_exchange(string):
    return string[-1:] + string[1:-1] + string[:1]


print string_exchange('morning')


#6 Write a Python program to remove the characters which have odd index values of a given string

def odd_character_removal(string):
    result = ''
    for i in range(len(string)):
        if i % 2 == 0:
            result = result + string[i]

    print result


odd_character_removal('python')


#7 Write a Python program to count the occurrences of each word in a given sentence.

def word_occcurance(sentence):
    words = sentence.split()
    word_count = {}.fromkeys(words,0)

    for word in words:
        word_count[word]+=1

    print word_count

word_occcurance('the quick brown fox jumps over the lazy dog')


#8 string Reversal


def string_reverse(string):
    reversed_string = ''
    string_length = len(string)
    while string_length:
        reversed_string = reversed_string + string[string_length - 1]
        string_length = string_length - 1

    print reversed_string


string_reverse('hello')

#9 Write a Python program to reverse words in a string.

def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words("Hello World"))


#10 Write a Python program to display a number with a comma separator.

x = 5000000
y = 50000000
print("\nOriginal Number: ", x)
print("Formatted Number with comma separator: "+"{:,}".format(x));
print("Original Number: ", y)
print("Formatted Number with comma separator: "+"{:,}".format(y));
