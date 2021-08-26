# Ram Reddy
# August 26th 2021

# Warmup 1
def sleep_in(weekday, vacation):
  return True if weekday == False or (weekday == True and vacation == True) else False

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  return a+b if a != b else 2*(a+b)

def diff21(n):
  return 21 - n if n <= 21 else 2 * (n - 21)

def parrot_trouble(talking, hour):
  return True if talking == True and (hour < 7 or hour > 20) else False

def makes10(a, b):
  return True if a == 10 or b == 10 or a + b == 10 else False

def near_hundred(n):
  return True if abs(100 - n) <= 10 or abs(200 - n) <= 10 else False

def pos_neg(a, b, negative):
  return True if negative == False and ((a > 0 and b < 0) or (a < 0 and b > 0)) or (negative == True and a < 0 and b < 0) else False

# String 1
def hello_name(name):
  return "Hello " + name +"!"

def make_abba(a, b):
  return a+b+b+a

def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

def make_out_word(out, word):
  return out[0:int(len(out)/2)]+word+out[int(len(out)/2) :] # Grader doesnt allow "):" in the string substring

def extra_end(str):
  return str[-2:]*3

def first_two(str):
  return str[0:2]

def first_half(str):
  return str[0:int(len(str)/2)]

def without_end(str):
  return str[1:len(str)-1]

# List 1
def first_last6(nums):
  return True if 6 == (nums[0] if type(nums[0] == int) else 0) or 6 == (nums[-1] if type(nums[-1] == int) else 0) else False

def same_first_last(nums):
  return True if (len(nums) >= 1 and (str(nums[0]) == str(nums[-1]))) else False

def make_pi(n):
  return [int("31415926535897"[i]) for i in range(n) if i < n]

def common_end(a, b):
  return True if str(a[0]) == str(b[0]) or str(a[-1]) == str(b[-1]) else False

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  return nums[1:] + nums[:1]

def reverse3(nums):
  return nums[::-1]

def max_end3(nums):
  return [nums[0] for i in range (len(nums))] if nums[0] > nums[-1] else [nums[-1] for i in range (len(nums))]

# Logic 1
def cigar_party(cigars, is_weekend):
  return True if (is_weekend == False and cigars >= 40 and cigars <= 60) or (is_weekend == True and cigars >= 40) else False

def date_fashion(you, date):
  return 2 if ((you >= 8 or date >= 8) and (you > 2 and date > 2)) else 0 if (you <= 2 or date <= 2) else 1

def squirrel_play(temp, is_summer):
  return True if (temp >= 60 and temp <= (100 if is_summer == True else 90)) else False

def caught_speeding(speed, is_birthday):
  return 0 if (speed <= (60 if is_birthday == False else 65)) else 1 if (speed <= (80 if is_birthday == False else 85)) else 2

def sorta_sum(a, b):
  return a+b if a+b < 10 or a+b > 19 else 20

def alarm_clock(day, vacation):
  return "7:00" if day > 0 and day < 6 and vacation == False else "10:00" if ((day == 0 or day == 6) and vacation == False) or (vacation == True and day > 0 and day < 6) else "off"

def love6(a, b):
  return True if a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6 else False

def in1to10(n, outside_mode):
  return True if (outside_mode == False and n >= 1 and n <= 10) or (outside_mode == True and (n <= 1 or n >= 10)) else False
