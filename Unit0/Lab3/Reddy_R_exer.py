# Name: Ram Reddy
# Date: 09/10/2021
# Do not forget to change the file name -> Save as
import math
import string
import PIL
from PIL import Image
import urllib.request
import io

# ''' Tasks '''
# # 1. Given an input of a space-separated list of any length of integers, output the sum of them.
# # 2. Output the list of those integers (from #1) that are divisible by three.
# msg = input("nums: ")
# print (msg)
# print (msg.split())
# print ([int(x) for x in msg.split()]) #list comprehension
# print (sum([int(x) for x in input("list of numbers: ").strip().split()])) # #1
# print ([int(x) for x in input("list of numbers: ").strip().split() if int(x) % 3 == 0]) # #2



# # 3. Given an integer input, print the first n Fibonacci numbers. eg. n=6: 1, 1, 2, 3, 5, 8
# amount = int(input("n: "))
# x = 0
# y = 1
# temp = 0
# for i in range(amount):
#     if i != 0:
#         temp = x
#         x = y
#         y = x+temp
#     print(y)

# # 4. Given an input, output a string composed of every other character. eg. Aardvark -> Arvr
# print(str(input("string: "))[::2])


# # 5. Given a positive integer input, check whether the number is prime or not.
# number = int(input("Positive integer: "))
# if len([0 for i in range(2, int(math.sqrt(number))+1) if number%i==0])>0:
#     print("Not Prime")
# else:
#     print("Prime")


# # 6. Calculate the area of a triangle given three side lengths.  eg. 13 14 15 -> 84
# arr = [int(x) for x in input("3 numbers: ").split()]
# semiP = (arr[0]+arr[1]+arr[2])/2
# area = math.sqrt(semiP*(semiP-arr[0])*(semiP-arr[1])*(semiP-arr[2]))
# print(int(area))

# # 7. Given a input of a string, remove all punctuation from the string. 
# # eg. "Don't quote me," she said. -> Dontquotemeshesaid
# msg = input("String: ")
# msg = "".join(i for i in msg if i not in string.punctuation).replace(" ", "")
# print(msg)

# # 8. Check whether the input string (from #7, lower cased, with punctuation removed) is a palindrome.
# msg = msg.lower()
# print(msg == msg[::-1])

# # 9. Count the number of each vowel in the input string (from #7).
# print(sum(msg.count(i) for i in "aeiou" if i in msg))
 
# # 10. Given two integers as input, print the value of f\left(k\right)=k^2-3k+2 for each integer between the two inputs.  
# # eg. 2 5 -> 0, 2, 6, 12
# i, j = input("Two numbers: ").split()
# for k in range(int(i), int(j)+1):
#     print(k**2-3*k+2)
    
# # 11. Given an input of a string, determines a character with the most number of occurrences.
# msg = input("String: ")
# temp = set(msg)
# var = 'a'
# for i in temp:
#     if msg.count(i) > msg.count(var):
#         var = i
# print(var)

# # 12. With the input string from #11, output a list of all the words that start and end in a vowel.
# words = msg.split()
# vowels = "aeiou"
# for w in words:
#     if w[0] in vowels and w[-1] in vowels:
#         print(w)

# # 13. With the input string from #11, capitalizes the starting letter of every word of the string and print it.
# print(msg.title())

# # 14. With the input string from #11, prints out the string with each word in the string reversed.
# for w in words:
#     print(w[::-1])

# # 15. With the input string from #11, treats the first word of the input as a search string to be found in the rest 
# # of the string, treats the second word as a replacement for the first, and treats the rest of the input as the string to be searched.
# # 	eg.    b Ba baby boy ->  BaaBay Baoy


 
# # 16. With an input of a string, removes all duplicate characters from a string.  Eg. detection -> detcion
# print("".join(dict.fromkeys(input("String: "))))

# # 17. Given an input of a string, determines whether the string contains only digits.
# # 18. If #17 prints True, determines whether the string contains only 0 and 1 characters, and if so assumes it is a binary string, 
# # converts it to a number, and prints out the decimal value.

# msg = input("String: ")
# arr = [i for i in msg if i in "0123456789"]
# if len(arr)==msg:
#     print("True")
#     temp = set(msg)
#     if len(temp) == 2:
#         if "0" in temp and "1" in temp:
#             print(int(msg, 2))
# else:
#     print("False")

# # 19. Write a script that accepts two strings as input and determines whether the two strings are anagrams of each other.
# msg, msg1 = input("Input two string: ").split()
# if sorted(msg.lower()) ==sorted(msg1.lower()):
#     print("True")
# else:
#     print("False")

# # 20. Given an input filename, if the file exists and is an image, find the dimensions of the image.
# filename = io.BytesIO(urllib.request.urlopen(input("Input file url: ")).read())
# try:
#     im = Image.open(filename)
#     im.verify()
#     print(im.size)
#     im.close()
# except:
#     print("Invalid image please try again.")


# # 21. Given an input of a string, find the longest palindrome within the string.
# def findLargestPalindrome(string, largest):
#     print(string[1:])
#     print(string[:-1])
#     if len(string) > 1 and len(string)>largest and string == string[::-1]:
#         largest = len(string)
#     elif len(string)> 1:
#         temp = findLargestPalindrome(string[1:], largest)
#         if temp>largest:
#             largest = temp
#         temp = findLargestPalindrome(string[:-1], largest)
#         if temp>largest:
#             largest = temp
#     return largest

# print(findLargestPalindrome(str(input("Give a string: ")), 0))

 
# # 22. Given an input of a string, find all the permutations of a string.
# def permute(string, permutations, level):
#     if(level==len(string)):
#         permutations.append(''.join(string))

#     for i in range(level, len(string)):
#         arr = list(string)
#         arr[i], arr[level] = arr[level], arr[i]
#         permute(arr, permutations, level+1)
    
#     return permutations
# permutations=permute(str(input("Input string: ")), [], 0)
# print(permutations)

# # 23. Given the input string from #22, find all the unique permutations of a string.
# print(list(set(permutations)))

 
# # 24. Given an input of a string, find a longest non-decreasing subsequence within the string (according to ascii value).
# msg = str(input("Input string: "))
# print(msg)
# arr = [ord(i) for i in msg]
# temp, max = 0, []
# for i in range(len(arr)):
#     if i ==0:
#         temp += 1
#     elif(arr[i-1] <= arr[i]):
#         temp+=1
#     elif(len(max) < temp):
#         max = arr[i-temp:i]
#         temp = 0
# print("".join(chr(i) for i in max))
        