# Ram Reddy
# August 31st 2021

# Warmup 2
def string_times(s, n):
    return s*n


def front_times(s, n):
    return s[:3]*n


def string_bits(s):
    return s[::2]


def string_splosion(l):
    return ''.join([l[:i] for i in range(len(l)+1)])


def last2(s):
    return sum([[0,1][s[i:i+2]==s[len(s)-2:]] for i in range(len(s)-2)])


def array_count9(n):
    return n.count(9)


def array_front9(n):
    return 9 in n[:4]


def array123(nums):
    return [False,True][sum([[0,1][nums[i:i+3]==[1,2,3]] for i in range(len(nums))])>0]


def string_match(a, b):
    return sum([[0,1][a[i:i+2]==b[i:i+2]] for i in range(len([b,a][len(a)>len(b)])-1)])

# Logic 2


def make_bricks(small, big, goal):
    return not(goal>big*5+small or goal%5>small)


def lone_sum(a, b, c):
    return sum([[0,i][[a,b,c].count(i)==1] for i in [a,b,c]])


def lucky_sum(a, b, c):
    return sum([a,b,c][:[a,b,c].index(13) if 13 in [a,b,c] else 3])


def no_teen_sum(a, b, c):
    return a+b+c-sum([[0,[a,b,c].count(i)*i][i in [a,b,c]] for i in [13,14,17,18,19]])


def round_sum(a, b, c):
    return sum([int(round([i,i+1][i%5==0],-1)) for i in [a,b,c]])


def close_far(a, b, c):
    return (abs(b-a)<=1 and abs(b-c)>=2 and abs(c-a)>=2) or (abs(c-a)<=1 and abs(b-c)>=2 and abs(b-a)>=2)


def make_chocolate(small, big, goal):
    return [-1,goal-5*[big,int(goal/5)][int(goal/5)<=big]][5*[big,int(goal/5)][int(goal/5)<=big]+small>=goal]

# String 2


def double_char(s):
    return ''.join([2*i for i in s])


def count_hi(str):
    return str.count('hi')


def cat_dog(str):
    return str.count('cat')==str.count('dog')


def count_code(str):
    return sum([[0,1][str.lower()[i:i+4][:2]=='co' and str.lower()[i:i+4][3]=='e'] for i in range(len(str)-3)])


def end_other(a, b):
  return b.lower()[::-1]==a.lower()[::-1][:len(b)] or a.lower()[::-1]==b.lower()[::-1][:len(a)]


def xyz_there(s):
    return 'xyz' in s.replace('.xyz','_')

# List 2


def count_evens(nums):
    return len(nums)-sum([i%2 for i in nums])


def big_diff(nums):
    return max(nums)-min(nums)


def centered_average(nums):
    return (sum(nums)-min(nums)-max(nums))//(len(nums)-2)
    #return sum(sorted(nums)[1:len(nums)-1])//(len(nums)-2)

def sum13(nums):
    return sum([[0,j][(i==0 and j!=13) or (i>0 and (j!=13 and nums[i-1]!=13))] for i, j in enumerate(nums)])


def sum67(nums):
    return sum([m for n,m in enumerate(nums) if n not in [k for i,j in enumerate(nums) if j==6 for k in range(nums.index(6,i,len(nums)),nums.index(7,i,len(nums))+1)]])

def has22(nums):
    return (2,2) in zip(nums,nums[1:])
