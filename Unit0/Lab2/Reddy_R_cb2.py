# Ram Reddy
# August 31st 2021

# Warmup 2
def string_times(str, n):
    return str*n


def front_times(str, n):
    return str[0:3]*n


def string_bits(str):
    return str[::2]


def string_splosion(var):
    return ''.join([var[0:i] for i in range(1, len(var)+1)])


def last2(str):
    return sum([1 if str[i:i+2] == str[len(str)-2:] else 0 for i in range(len(str)-2)])


def array_count9(nums):
    return nums.count(9)


def array_front9(nums):
    return True if(9 in nums[0:4]) else False


def array123(nums):
    return True if(sum([1 if nums[i:i+3] == [1, 2, 3] else 0 for i in range(len(nums))]) > 0) else False


def string_match(a, b):
    return sum([1 if a[i:i+2] == b[i:i+2] else 0 for i in range(len(a if len(a) > len(b) else b)-1)])

# Logic 2


def make_bricks(small, big, goal):
    return False if goal > big*5 + small else False if goal % 5 > small else True


def lone_sum(a, b, c):
    return sum([i if [a, b, c].count(i) == 1 else 0 for i in [a, b, c]])


def lucky_sum(a, b, c):
    return sum([a, b, c][0:[a, b, c].index(13) if 13 in [a, b, c] else 3])


def no_teen_sum(a, b, c):
    return a+b+c - sum([[a, b, c].count(i)*i if i in [a, b, c] else 0 for i in [13, 14, 17, 18, 19]])


def round_sum(a, b, c):
    return sum([int(round(i, -1)) for i in [a, b, c]])


def close_far(a, b, c):
    return True if(abs(b-a) <= 1 and abs(b-c) >= 2 and abs(c-a) >= 2) else True if(abs(c-a) <= 1 and abs(b-c) >= 2 and abs(b-a) >= 2) else False


def make_chocolate(small, big, goal):
    return (goal-5 * (int(goal/5) if int(goal/5) <= big else big)) if(5*(int(goal/5) if int(goal/5) <= big else big) + small >= goal) else -1

# String 2


def double_char(str):
    return "".join([2*i for i in str])


def count_hi(str):
    return str.count("hi")


def cat_dog(str):
    return True if ((str.count("cat")) == (str.count("dog"))) else False


def count_code(str):
    return sum([1 if str.lower()[i:i+4][0:2] == "co" and str.lower()[i:i+4][3] == "e" else 0 for i in range(len(str)-3)])


def end_other(a, b):
    return True
#   return True if ((len(a) >= len(b)) and a[len(a)-len(b) :len(a)].lower()==b.lower()) else True if ((len(a) < len(b)) and b[len(b)-len(a) :len(b)].lower()==a.lower()) else  False


def xyz_there(str):
    return True if(str.replace(".xyz", "_").count("xyz") > 0) else False

# List 2


def count_evens(nums):
    return len(nums) - sum([i % 2 for i in nums])


def big_diff(nums):
    return max(nums) - min(nums)


def centered_average(nums):
    return int(sum(sorted(nums)[1:len(nums)-1])/(len(nums)-2))


def sum13(nums):
    return sum([j if (i == 0 and j != 13) or (i > 0 and (j != 13 and nums[i-1] != 13)) else 0 for i, j in enumerate(nums)])


def sum67(nums):
    return [(nums[i]) if i % 2 == 0 else 0 for i in range(len(nums))]


def has22(nums):
    return (2, 2) in zip(nums, nums[1:])
