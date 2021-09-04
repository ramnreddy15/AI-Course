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


def array123(n):
    return sum([[0,1][n[i:i+3]==[1,2,3]] for i in range(len(n))])>0


def string_match(a, b):
    return sum([[0,1][a[i:i+2]==b[i:i+2]] for i in range(len([b,a][len(a)>len(b)])-1)])

# Logic 2


def make_bricks(s, b, g):
    return not(g>b*5+s or g%5>s)


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


def make_chocolate(s, b, g):
    return [-1,g-5*[b,int(g/5)][int(g/5)<=b]][5*[b,int(g/5)][int(g/5)<=b]+s>=g]

# String 2


def double_char(s):
    return ''.join([2*i for i in s])


def count_hi(s):
    return s.count('hi')


def cat_dog(s):
    return s.count('cat')==s.count('dog')


def count_code(s):
    return sum([[0,1][s.lower()[i:i+4][:2]=='co' and s.lower()[i:i+4][3]=='e'] for i in range(len(s)-3)])


def end_other(a, b):
  return b.lower()[::-1]==a.lower()[::-1][:len(b)] or a.lower()[::-1]==b.lower()[::-1][:len(a)]


def xyz_there(s):
    return 'xyz' in s.replace('.xyz','_')

# List 2


def count_evens(n):
    return len(n)-sum([i%2 for i in n])


def big_diff(n):
    return max(n)-min(n)


def centered_average(n):
    return (sum(n)-min(n)-max(n))//(len(n)-2)
    #return sum(sorted(nums)[1:len(nums)-1])//(len(nums)-2)

def sum13(n):
    return sum([[0,j][(i==0 and j!=13) or (i>0 and (j!=13 and n[i-1]!=13))] for i, j in enumerate(n)])


def sum67(u):
    return sum([m for n,m in enumerate(u) if n not in [k for i,j in enumerate(u) if j==6 for k in range(u.index(6,i,len(u)),u.index(7,i,len(u))+1)]])

def has22(n):
    return (2,2) in zip(n,n[1:])
