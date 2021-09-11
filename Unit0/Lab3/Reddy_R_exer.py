# Name: Ram Reddy
# Date: 09/10/2021
# Do not forget to change the file name -> Save as
import math
import string
from PIL import Image

# ''' Tasks '''
# 1. Given an input of a space-separated list of any length of integers, output the sum of them.
# 2. Output the list of those integers (from #1) that are divisible by three.
msg = [int(x) for x in input("list of numbers: ").strip().split()]
print("1. sum =", sum(msg))  # 1
print("2. list of multiples of 3:", [int(x)
      for x in msg if int(x) % 3 == 0])  # 2


# 3. Given an integer input, print the first n Fibonacci numbers. eg. n=6: 1, 1, 2, 3, 5, 8
amount = int(input("Type n for Fibonacci sequence: "))
print("3. fibonacci: ", end="")
x, y, temp = 0, 1, 0
for i in range(amount):
    if i != 0:
        temp = x
        x = y
        y = x+temp
    print(y, end=" ")
print("", end="\n")

# 4. Given an input, output a string composed of every other character. eg. Aardvark -> Arvr
print("4. every other string:", str(input("Type a string: "))[::2])


# 5. Given a positive integer input, check whether the number is prime or not.
number = int(input("Type a number to check prime: "))
if len([0 for i in range(2, int(math.sqrt(number))+1) if number % i == 0]) > 0:
    print("5. Is prime?", False)
else:
    print("5. Is prime?", True)


# 6. Calculate the area of a triangle given three side lengths.  eg. 13 14 15 -> 84
arr = [int(x) for x in input("Type three sides of a triangle: ").split()]
semiP = (arr[0]+arr[1]+arr[2])/2
area = math.sqrt(semiP*(semiP-arr[0])*(semiP-arr[1])*(semiP-arr[2]))
print("6. The area of", arr[0], arr[1], arr[2], "is", area)

# 7. Given a input of a string, remove all punctuation from the string.
# eg. "Don't quote me," she said. -> Dontquotemeshesaid
msg = input("Type a sentence: ")
msg = "".join(i for i in msg if i not in string.punctuation).replace(" ", "")
print("7. Funct removed:", msg)

# 8. Check whether the input string (from #7, lower cased, with punctuation removed) is a palindrome.
msg = msg.lower()
print("8. Is Palindrome?", msg == msg[::-1])

# 9. Count the number of each vowel in the input string (from #7).
print("9. Count each voewl:", {i: msg.count(i) for i in "aeiou"})

# 10. Given two integers as input, print the value of f\left(k\right)=k^2-3k+2 for each integer between the two inputs.
# eg. 2 5 -> 0, 2, 6, 12
i, j = input("Type two integers (lower bound and upper bound): ").split()
print("10. Evaluate f(k)=k^2 - 3k + 2 from {} to {}:".format(i, j), end=" ")
for k in range(int(i), int(j)+1):
    print(k**2-3*k+2, end=" ")
print()

# 11. Given an input of a string, determines a character with the most number of occurrences.
msg = input("Type a string: ")
temp = {i: msg.count(i) for i in set(msg)}
temp2 = sorted(temp.values())
print("11. Most occured char:", " ".join(
    sorted([i for i in temp.keys() if temp[i] == temp2[-1]], reverse=True)))

# 12. With the input string from #11, output a list of all the words that start and end in a vowel.
words = msg.split()
vowels = "aeiou"
print("12. List of words starting and ending with vowels:", [
      w for w in words if w[0] in vowels and w[-1] in vowels])

# 13. With the input string from #11, capitalizes the starting letter of every word of the string and print it.
print("13. Capitalize starting letter of every word:", msg.title())

# 14. With the input string from #11, prints out the string with each word in the string reversed.
print("14. Reverse every word:", end=" ")
for w in words:
    print(w[::-1], end=" ")
print()

# 15. With the input string from #11, treats the first word of the input as a search string to be found in the rest
# of the string, treats the second word as a replacement for the first, and treats the rest of the input as the string to be searched.
# 	eg.    b Ba baby boy ->  BaaBay Baoy
print("15. Find the first and replace with the second:", " ".join(
    words[i].replace(words[0], words[1]) for i in range(2, len(words))))


# 16. With an input of a string, removes all duplicate characters from a string.  Eg. detection -> detcion
print("16. Remove all duplicat chars:", "".join(dict.fromkeys(
    input("Type a string to remove all duplicate chars: "))))

# 17. Given an input of a string, determines whether the string contains only digits.
# 18. If #17 prints True, determines whether the string contains only 0 and 1 characters, and if so assumes it is a binary string,
# converts it to a number, and prints out the decimal value.

msg = input("Type a string to check if it has only digits or not: ")
arr = [i for i in msg if i in "0123456789"]
if len(arr) == len(msg):  # 17
    print("17. Is a number?: True")
    temp = set(msg)
    print("18. It is a binary number:", end=" ")
    if len(temp) == 2:  # 18
        if "0" in temp and "1" in temp:
            print(int(msg, 2))
        else:
            print("Not binary.")
    else:
        print("Not binary.")
else:
    print("17. Is a number?: False")

# 19. Write a script that accepts two strings as input and determines whether the two strings are anagrams of each other.
msg = input("Type the first string to check anagram: ")
msg1 = input("Type the second string to check anagram: ")
print("19. Are {} and {} anagram?:".format(msg, msg1), end=" ")
if sorted(msg.lower()) == sorted(msg1.lower()):
    print("True")
else:
    print("False")

# 20. Given an input filename, if the file exists and is an image, find the dimensions of the image.
filename = input("Type the image file address: ")
try:
    im = Image.open(filename)
    im.verify()
    print("20. Image dimension: {} by {}".format(im.width, im.height))
    im.close()
except:
    print("20. Invalid image please try again.")


# 21. Given an input of a string, find the longest palindrome within the string.
def findLargestPalindrome(string, largest):
    if len(string) > 1 and len(string) > len(largest) and string == string[::-1]:
        largest = string
    elif len(string) > 1:
        if len(string[1:]) > len(largest):
            temp = findLargestPalindrome(string[1:], largest)
            if len(temp) > len(largest):
                largest = temp
        if len(string[:-1]) > len(largest):
            temp = findLargestPalindrome(string[:-1], largest)
            if len(temp) > len(largest):
                largest = temp
    return largest


print("21. Longest palindrome within the string:", findLargestPalindrome(str(
    input("Type a string to find the longest palindrome: ")).replace(" ", ""), ""))


# 22. Given an input of a string, find all the permutations of a string.
def permute(string, permutations, level):
    if(level == len(string)):
        permutations.append(''.join(string))

    for i in range(level, len(string)):
        arr = list(string)
        arr[i], arr[level] = arr[level], arr[i]
        permute(arr, permutations, level+1)

    return permutations


permutations = permute(str(input("Type a string to do permutation: ")), [], 0)
print("22. all permutations:", permutations)

# 23. Given the input string from #22, find all the unique permutations of a string.
print("23. all unique permutations:", list(set(permutations)))


# 24. Given an input of a string, find a longest non-decreasing subsequence within the string (according to ascii value).
msg = str(input("Type a string to find the longest non-decreasing sub: "))
print(msg)
arr = [ord(i) for i in msg]
temp, max = 0, []
for i in range(len(arr)):
    if i == 0:
        temp += 1
    elif(arr[i-1] <= arr[i]):
        temp += 1
    elif(len(max) < temp):
        max = arr[i-temp:i]
        temp = 0
print("24. longest non-decreasing sub:", "".join(chr(i) for i in max))
